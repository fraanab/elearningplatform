from core.views import add_video, create_course, delete_video
from django.urls import path

from . import views

urlpatterns = [
	path('', views.courses, name="courses-page"),
	path('course/<slug:slug>/', views.course, name="course-page"),
	path('course/payment/<str:id>/', views.course_payment, name="course-payment"),
	path('create_course/', create_course, name='create_course'),
	path('add_video/', add_video, name='add_video'),
	path('delete_video/<int:id>/', delete_video, name='delete_video'),
	path('create_comment/<slug:slug>/', views.create_comment, name="create_comment"),
	path('delete_comment/<int:id>/', views.delete_comment, name="delete_comment")
]
