from django.urls import path
import views

app_name = 'contacts'
urlpatterns = [   
    path('<int:cont_id>', views.single_contact, name='single_contact'),
    path('', views.index, name='index'),
]