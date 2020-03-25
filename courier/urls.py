from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', views.home,name="home"),
    path('student/<str:pk_test>/',views.student,name="student"),
    path('company/',views.company,name="company"),
    path('create_courier/<str:pk>/',views.createCourier,name='create_courier'),
    path('update_courier/<str:pk>/',views.updateCourier,name='update_courier'),
    path('remove_courier/<str:pk>/',views.deleteOrder,name='remove_courier'),
    path('update_student/<str:pk>/',views.updateStudent,name='update_student'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('user/',views.userPage,name='user-page'),
    path('logout/',views.logoutUser,name='logout'),
    path('user_settings/',views.userSetting,name='user_settings'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('admin_complaint/',views.comp_admin,name='admin_complaint'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="courier/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="courier/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="courier/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="courier/password_reset_done.html"),
        name="password_reset_complete"),
]
