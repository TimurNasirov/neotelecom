from django.shortcuts import render, get_object_or_404

from applications.core.models import City
from applications.promotions.models import Promotion


def promotion_detail_view(request, promotion_id):
    promotion = get_object_or_404(Promotion, pk=promotion_id)
    return render(request, 'actions/promotion_details.html', context={'promotion': promotion})


def promotion_list_view(request):
    city_slug = request.COOKIES.get('city') or 'bishkek'
    city = City.objects.filter(slug=city_slug).last()
    promotions = Promotion.production.filter(city=city)
    return render(request, 'actions/promotion_list.html', context={'promotions': promotions})
