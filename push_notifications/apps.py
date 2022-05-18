from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BeriaConfig(AppConfig):
    name = 'push_notifications'
    verbose_name = _('Push Notifications')
