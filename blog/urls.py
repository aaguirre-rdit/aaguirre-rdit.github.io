from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('projects',views.projects, name='projects'),
    path('about',views.about, name='about'),
    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('category/<int:pk>/',views.category_filter, name='category_filter')
]
