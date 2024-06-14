from django.conf import settings


def global_settings(request):
    return {'INSTANCE': settings.APP_INSTANCE}
