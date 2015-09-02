import datetime

from info.models import Info, ActionInfo
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


def create_info_signal(action, sender_info, **kwargs):
    ActionInfo.objects.create(
        date=datetime.datetime.today(),
        action_name=action,
        object_name=sender_info.__name__,
        object_info=kwargs['instance'].first_name +
        ' ' + kwargs['instance'].last_name,
            )


@receiver(post_save, sender=Info)
def save_person_info(sender, **kwargs):
    if kwargs['created'] == True:
        create_info_signal('save', sender, **kwargs)
    else:
        create_info_signal('edit', sender, **kwargs)


@receiver(pre_delete, sender=Info)
def delete_person_info(sender, **kwargs):
    create_info_signal('delete', sender, **kwargs)
