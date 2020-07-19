from django.shortcuts import render, redirect
from .models import Subscribe
from .forms import SubscribeForm


def index(request):
#    tasks = Task.objects.order_by('-id')
#    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def about(request):
    return render(request, 'main/about.html')


def thank(request):
    return render(request, 'main/thank.html')


def category(request):
    return render(request, 'main/category.html')



def subscribe(request):
    error = ''
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank')
        else:
            error = 'Форма була неправильною'

    form = SubscribeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/subscribe.html', context)
