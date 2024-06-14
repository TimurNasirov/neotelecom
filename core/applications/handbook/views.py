from django.http import Http404
from django.shortcuts import render

from applications.handbook.models import HandBook


def handbook_category_view(request, category):
    answers = HandBook.objects.filter(category=category).all()
    if not answers:
        raise Http404

    return render(request, 'handbook/handbook-category.html', context={
        'answers': answers,
        'category': category,
        'category_title': answers.last().get_category_display()
    })


def handbook_view(request):
    categories = HandBook.objects.all()
    return render(request, 'handbook/handbook.html', context={ 'categories': categories })