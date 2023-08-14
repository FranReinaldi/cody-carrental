from django.urls import path
from .views import (register, profile, delete_account,
                    check_email, change_password,
                    CustomLoginView, CustomLogoutView)


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
    path('check_email/', check_email, name='check_email'),
    path('change_password/', change_password, name='change_password'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
