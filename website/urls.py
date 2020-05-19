from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
]
