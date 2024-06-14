from django.shortcuts import render

from applications.channels.models import Channel


def channels_view(request):
    channels = Channel.objects.all()
    return render(request, 'channels/channels.html', context={'channels': channels})
