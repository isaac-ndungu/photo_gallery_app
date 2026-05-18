from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    profile_view, CustomPasswordChangeView, CustomPasswordChangeDoneView,
    public_profile_view
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('user/<str:username>/', public_profile_view, name='public_profile'),
]