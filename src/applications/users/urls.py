from django.urls import path
from .views import (register, profile, delete_account,
                    CustomLoginView, CustomLogoutView)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
]
