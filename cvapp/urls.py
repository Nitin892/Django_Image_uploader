from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signupform'),
    path('login/',views.login,name='loginform'),
    path('logout/',views.logout,name='logoutform'),
    path('getphotos/',views.getPhotos,name='getphotos'),
    path('postphoto/', views.postphoto, name='postphoto'),
    path('getphotos/<int:id>/', views.updatephoto, name='updatephoto'),
    path('deletephotos/<int:id>/', views.deletephoto, name='deletephoto'),
    path('profile/',views.profile,name='profile'),
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name='cvapp/passwordrest.html'),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='cvapp/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='cvapp/password_reset_form.html'),name='password_reset_confirm'),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='cvapp/password_rest_done.html'),name='password_reset_complete'),

]