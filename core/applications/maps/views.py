from django.http import JsonResponse, Http404
from django.shortcuts import render

from applications.maps.models import Map


def map_view(request, map_type):
    if map_type not in ['4g', 'gpon', 'smart_tv']:
        raise Http404
    return render(request, 'maps/map.html', {'map_type': map_type})


def get_map_coordinates(request, map_type):
    context = {'success': False, 'data': []}
    map_objects = Map.objects.filter(map_type=map_type).all()
    if map_objects.count() <= 0:
        return JsonResponse(context)

    data = [map_obj.get_coordinates() for map_obj in map_objects]
    context.update({'success': True, 'map_data': data})
    return JsonResponse(context, safe=True)
