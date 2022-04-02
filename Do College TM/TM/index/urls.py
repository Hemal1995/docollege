from django.conf.urls import url 
from django.urls import path
from index import views

urlpatterns = [
    path('', views.start, name = 'start'),
    path('finish/', views.finish, name = 'finish'),
    path('record/', views.record, name = 'record'),
    path('time/', views.time_record, name = 'time_record'),
    path('Hiroyuki/', views.Hiroyuki, name='Hiroyuki'),
    path('Shotaro/', views.Shotaro, name='Shotaro'),
    path('Rui/', views.Rui, name='Rui'),
    path('Shinnosuke/', views.Shinnosuke, name='Shinnosuke'),
    path('Hito/', views.Hito, name='Hito'),
    path('Aina/', views.Aina, name='Aina'),
    path('Masaya/', views.Masaya, name='Masaya'),
    path('Kenji/', views.Kenji, name='Kenji'),
    path('Ryusei/', views.Ryusei, name='Ryusei'),
    path('Kento/', views.Kento, name='Kento'),
    path('Hiroshi/', views.Hiroshi, name='Hiroshi'),
    path('Shizuka/', views.Shizuka, name='Asahi'),
    path('Asahi/', views.Asahi, name='Asahi'),
]