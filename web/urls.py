from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('page/',views.page, name='page'),
    path('page/<str:section>',views.page, name='page'),
    path('upload_csv/',views.upload_csv, name='upload_csv'),
]
