from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('campus_dropdown/', views.campus_dropdown, name='campus_dropdown'),
    path('answer/', views.answer_view, name='answer'),
    path('checkin/', views.check_in, name='checkin'),
]
