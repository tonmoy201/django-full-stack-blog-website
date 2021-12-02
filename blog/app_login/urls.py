from django.urls import path
from .import views
app_name="app_login"
urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile,name='profile'),
    path('edit-profile/',views.edit_profile,name='edit_profile'),
    path('password/',views.password_change,name="password"),
    path('add-pic/',views.pro_pic_change,name="addpic"),
    
]