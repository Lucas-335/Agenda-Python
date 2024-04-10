from django.urls import path
from contacts import views

app_name = 'contacts'
urlpatterns = [   
    path('search/',views.search, name='search'),
    path('', views.index, name='index'),

    #contact CRUD
    path('contact/<int:cont_id>', views.single_contact, name='single_contact'),
    path('contact/create', views.create, name='create'),
]