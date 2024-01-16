from django.urls import path, include

import homeworks_app1.views

app_name = 'homeworks_app1'

urlpatterns = [
    path('', homeworks_app1.views.index, name='index'),
    path('myself/', homeworks_app1.views.about_myself, name='myself'),
]
