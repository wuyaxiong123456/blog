from django.urls import path
from blog_zhaojianbing import views

app_name = 'blog_zhaojianbing'

urlpatterns = [
    path('',views.Post_list,name = 'post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name = 'post_detail'),

]