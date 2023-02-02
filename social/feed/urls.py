from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed_page, name='feed'),
    path('login/', views.login_page),
    path('logout/', views.logout_page),
    path('registration/', views.registration_page),
    path('user/<pk>/', views.UserDetailView.as_view()),
    path('delete/<int:id>/', views.delete_post, name="delete_post"),
]