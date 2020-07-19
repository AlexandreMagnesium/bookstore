from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('category', views.category, name='category'),
    path('thank', views.thank, name='thank'),

#    path('books', views.books, name='books'),
#    path('e-books', views.e_books, name='e-books'),
#    path('sale', views.sale, name='sale'),
#    path('t-shirts', views.t_shirts, name='t-shirts'),

#    path('create', views.create, name='create'),
]
