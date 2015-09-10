from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, render
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.db.models import Q

from info.models import Info, UserRequest, ActionInfo, UserInvite
from info.forms import InfoForm, MyUserCreationForm

from braces.views import GroupRequiredMixin, LoginRequiredMixin


class InfoDetailView(DetailView):
    template_name = 'info/information.html'
    context_object_name = 'info'

    def get_object(self):
        obj = self.request.user.info.all().first()
        return obj


class LatestRequestListView(GroupRequiredMixin, ListView):
    model = UserRequest
    template_name = 'info/latest_request.html'
    context_object_name = 'list'
    group_required = "dev"

    def get_queryset(self):
        qs = super(LatestRequestListView, self).get_queryset()
        qs = qs.order_by('-time')[:15]
        return qs


class InfoCreationView(LoginRequiredMixin, CreateView):
    model = Info
    template_name = 'info/create_info.html'
    form_class = InfoForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InfoCreationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('info')


class InfoUpdateView(LoginRequiredMixin, UpdateView):
    model = Info
    form_class = InfoForm
    template_name = 'info/edit.html'

    def get_success_url(self):
        return reverse('info')


def login_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        possible_user = User.objects.filter(
                (Q(email=username_or_email) | Q(username=username_or_email)) &
                Q(is_active=True)).first()
        if possible_user is None:
                error_msg = _('Username/password is wrong')
        else:
            user = authenticate(username=possible_user.username,
                                password=password)
            if user = 'AnonymousUser':
                error_msg = _('Username/password is wrong')
            else:
                login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        return render_to_response('registration/login.html', {}, context)
    return render_to_response('registration/login.html', {
                            'username_or_email': username_or_email,
                            'password': password,
                            'error_msg': error_msg},
                             context)


class RegisterFormView(FormView):
    form_class = MyUserCreationForm
    template_name = "registration/registration_form.html"

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        user = authenticate(username=self.request.POST['username'],
                            password=self.request.POST['password1'])
        login(self.request, user)
        send_mail('Congratulations!!',
                  'Hi! You are register in our web-site.' + '\n' +
                  self.request.build_absolute_uri(reverse('index')),
                  'admin@minisite.com',
                  [self.request.POST['email']])
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('create_info')


class InviteRegisterFormView(RegisterFormView):

    def form_valid(self, form):
        form.save()
        invite = get_object_or_404(UserInvite, code=self.kwargs['code'])
        invite.is_accept = True
        invite.save()
        email = self.request.POST['email']
        user = authenticate(username=self.request.POST['username'],
                            password=self.request.POST['password1'])
        login(self.request, user)
        send_mail('Congratulations!!',
                  'Hi! You are register in our web-site.' + '\n' +
                  self.request.build_absolute_uri(reverse('index')),
                  'admin@minisite.com',
                  [self.request.POST['email']])
        return super(InviteRegisterFormView, self).form_valid(form)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def invite(request):
    translation.activate(request.POST['language'])
    if request.method == 'POST':
        email = request.POST['email']
        response_data = {}
        if request.user.is_authenticated() == False:
                msg_value = _("Please authenticate in the site")
        elif User.objects.filter(email=email).exists():
                msg_value = _("User with this email are register")
        elif UserInvite.objects.filter(Q(email=email) & Q(user=request.user) |
                                       (Q(email=email) & Q(is_accept=True))).exists():
                msg_value = _("In this email Invite already sent")
        else:
            code = User.objects.make_random_password(
                        length=10,
                        allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQ')
            invite = UserInvite.objects.create(user=request.user,
                                               email=email,
                                               code=code)
            link = request.build_absolute_uri(reverse('register')) + code
            send_mail('Hi! This your invite.',
                      'Hi! You can register in our web-site.' + '\n' + link,
                      'admin@minisite.com', [email],
                      fail_silently=False)
            msg_value = _("Thank you for invite your friends!!!")
        response_data['msg'] = unicode(msg_value)
    return JsonResponse(response_data)
