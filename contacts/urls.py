from django.urls import path
from contacts import views

app_name = 'contacts'
urlpatterns = [   
    path('<int:cont_id>', views.single_contact, name='single_contact'),
    path('search/',views.search, name='search'),
    path('', views.index, name='index'),
]