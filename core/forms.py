from courses.models import Course, Video
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields= '__all__'
class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields= ['thumb', 'name', 'description']

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=255, required=True)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {
			'username': '',
			'email': '',
			'password1': '',
			'password2': '',
		}
