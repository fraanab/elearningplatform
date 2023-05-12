from django.contrib.auth import views
from django.urls import path

from .views import main, profile, signup

urlpatterns = [
	path('', main, name="frontpage"),
	path('signup/', signup, name="signup"),
	path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('profile/', profile, name="profile"),
]
