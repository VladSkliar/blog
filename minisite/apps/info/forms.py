from info.models import Info
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class InfoForm(ModelForm):
    class Meta:
        BIRTH_YEAR_CHOICES = range(1960, 2005)
        model = Info
        exclude = ('user',)
        error_messages = {
            'first_name': {
                'max_length': _("This first name is too long."),
                'required': _("Please enter your first name")
            },
            'last_name': {
                'max_length': _("This last name is too long."),
                'required': _("Please enter your last name")
            },
            'birthdate': {
                'required': _("Please enter your birthdate"),
                'invalid': _("Plese enter correct birthdate")
            },
            'bio': {
                'max_length': _("This last name is too long."),
                'required': _("Please enter your bio")
            }
            }


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", 'email')
