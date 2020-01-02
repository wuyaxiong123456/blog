from django.urls import path
from .views import index
from . import views

app_name = 'blog_wuyaxiong'
urlpatterns = [
    path('index/',index),
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    
]