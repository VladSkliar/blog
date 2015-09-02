from django.utils import timezone
from info.models import UserRequest


class HttpRequestSaver(object):

    def process_request(self, request):
        if request.method == 'GET' and request.path.startswith('/admin/') == False:
            UserRequest.objects.create(path=request.path, time=timezone.now())
            return None
