from django.urls import path
from . import views
from .views import BBLoginView, BBLogoutView, BBPasswordChangeView, RegisterDoneView, RegisterUserView

app_name = 'main'

urlpatterns = [
	path('', views.index),
	path('accounts/login/', BBLoginView.as_view(), name="login"),
	path('accounts/register/', RegisterUserView.as_view(), name='register'),
	path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
	path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
	path('accounts/logout/', BBLogoutView.as_view(), name="logout"),
]