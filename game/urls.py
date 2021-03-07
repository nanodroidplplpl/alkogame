from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ses_id>/', views.room, name='room'),
    path('get_new/', views.newses, name='newses'),
    #path('<int:ses_id>/game/add_score/', views.room, name='name'),
    path('test_photo', views.test_photo, name='test_photo'),
]
