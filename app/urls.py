from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('about_us/',views.about_us, name='about_us'),
    path("project/",views.project, name='project'),
    path('contact/',views.contact, name='contact')
]
