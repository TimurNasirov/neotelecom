from django.conf import settings

from applications.core.models import City


class CityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        default_city = settings.DEFAULT_CITY

        city_id = request.GET.get('city') or default_city
        city_id = request.session.get('city') or city_id

        city = City.objects.filter(id=city_id).last()

        if not city:
            city, _ = City.objects.get_or_create(title=settings.DEFAULT_CITY_TITLE)

        request.city = city

        response = self.get_response(request)

        return response
