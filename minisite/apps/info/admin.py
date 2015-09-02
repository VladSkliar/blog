from django.contrib import admin
from info.models import Info, UserRequest
from sorl.thumbnail.admin import AdminImageMixin


class InfoAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(UserRequest)
admin.site.register(Info, InfoAdmin)
