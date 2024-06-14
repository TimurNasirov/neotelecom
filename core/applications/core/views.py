from pathlib import Path

from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from applications.banners.models import Banner
from applications.core.forms import JoinUsForm
from applications.core.models import City, CallMe, Vacancy, NeoTvFiles, JoinUs
from applications.news.models import News
from applications.promotions.models import Promotion
from applications.tbot.integrator import TelegramBotIntegration


def main_page_view(request):
    banners = Banner.active_sliders.all()

    city_slug = request.COOKIES.get('city') or 'bishkek'
    city = City.objects.filter(slug=city_slug).last()
    promotions = Promotion.production.filter(city=city)

    # TODO: Это плохо, потом переделать.
    all_news = News.objects.all()[:5]
    tech_news = News.objects.filter(news_type='tech')[:5]
    media_news = News.objects.filter(news_type='media')[:5]

    return render(request, 'main.html', context={
        'banners': banners,
        'promotions': promotions,
        'all_news': all_news,
        'tech_news': tech_news,
        'media_news': media_news,
    })


def join_us_view(request):
    if request.method == 'POST':
        form = JoinUsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            text = (f'*Новая заявка на подключение:* \n'
                    f'Тип заявки: {obj.get_form_type_display()} \n'
                    f'Имя: {obj.name} \n'
                    f'Адрес: {obj.address} \n'
                    f'Номер телефона: {obj.phone} \n')

            TelegramBotIntegration().send_message(text, 'join_us', obj.pk)
            return render(request, 'join_us.html')

    form = JoinUsForm()
    return render(request, 'join_us.html', context={'form': form})


def city_switcher(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('city', city.slug, max_age=30 * 24 * 60 * 60)
    return response


def custom_handler404(request, *args, **kwargs):
    return render(request, 'common/404.html', status=404)


def custom_pages_view(request, page_name):
    if not Path(f'templates/pages/{page_name}.html').is_file():
        raise Http404
    return render(request, f'pages/{page_name}.html')


@csrf_exempt
def create_callback(request):
    context = {'success': False}
    if request.method != 'POST':
        return JsonResponse(context)

    name = request.POST.get('name') or None
    phone = request.POST.get('phone') or None

    if not name or not phone:
        return JsonResponse(context)

    try:
        obj = CallMe.objects.create(name=name, phone=phone)
        text = (f'*Заказан обратный звонок:* \n' #Исправлен опечатка Насировым Тимуром
                f'Имя: {obj.name} \n'
                f'Номер телефона: {obj.phone}. \n')
        TelegramBotIntegration().send_message(text, 'call_me', obj.pk)
    except:
        return JsonResponse(context)

    if obj:
        context.update({'success': True})

    return JsonResponse(context)


def vacancies_list(request):
    vac = Vacancy.objects.all()
    return render(request, f'vacancy/vacancy_list.html', context={'vacancies': vac})


def vacancies_detail(request, vacancies_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancies_id)
    return render(request, f'vacancy/vacancy_details.html', context={'vacancy': vacancy})


def neo_tv_view(request):
    context = {}
    for file in NeoTvFiles.objects.all():
        context.update({file.type: file.url.url})
    return render(request, f'pages/neotv.html', context=context)

#Добавлено Насировым Тимуром. Для связи телеграм @nicknamer091
@csrf_exempt
def add_join_us(request): #API для создания обьекта JoinUs
    if request.method == 'POST':
        try:
            _type = request.POST.get('type')
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            apikey = request.POST.get('apikey')
            if apikey == 'Kbe93juNe3odFOksMw94jbcVG6q49':
                obj = JoinUs.objects.create(form_type=_type, name=name, address=address, phone=phone)
                text = (f'*Новая заявка на подключение:* \n'
                    f'Тип заявки: {obj.form_type} \n'
                    f'Имя: {obj.name} \n'
                    f'Адрес: {obj.address} \n'
                    f'Номер телефона: {obj.phone} \n')

                TelegramBotIntegration().send_message(text, 'join_us', obj.id)
                return HttpResponse('Success!', status=201)
            else:
                return HttpResponse('Wrong apikey', status=403)
        except Exception:
            return HttpResponse('Not enough arguments', status=400)
    return HttpResponse('Invalid method', status=405)