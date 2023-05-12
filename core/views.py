from courses.models import UserCourse, Video
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

from .forms import CourseForm, SignUpForm, VideoForm


@cache_page(60*5)
def main(request):
	return render(request, 'main.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
		else:
			return render(request, 'signup.html', {'form':form, "error_msg": "There's been an error. Try again."})
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

@login_required
def profile(request):
	if request.user.is_superuser:

		video_form = VideoForm()
		course_form = CourseForm()
		users = User.objects.all().count()
		courses_bought = UserCourse.objects.all().count()
		total_profit = courses_bought * 25

		admin_data = {
			'video_form':video_form,
			'course_form':course_form,
			'all_users':users,
			'courses_bought':courses_bought,
			'total_profit': total_profit,
		}
		return render(request, 'admin-dashboard.html', admin_data)
	else:
		user_courses = UserCourse.objects.filter(user=request.user)
		return render(request, 'profile.html', {'courses':user_courses})


@login_required
def add_video(request):
	if request.user.is_superuser:
		video_form = VideoForm(request.POST, request.FILES)
		if video_form.is_valid():
			videoFile = request.FILES.get('video_file')
			video_form.video_file = videoFile
			video_form.save()
			return redirect(request.META['HTTP_REFERER'])
	else:
		return redirect('/')

@login_required
def create_course(request):
	if request.user.is_superuser:
		course_form = CourseForm(request.POST, request.FILES)
		if course_form.is_valid():
			thumbFile = request.FILES.get('thumb')
			course_form.thumb = thumbFile
			course_form.save()
			return redirect('courses-page')
		else:
			return JsonResponse({'message':'Invalid form data.'})

	else:
		return redirect('/')

@login_required
@require_http_methods(['POST'])
def delete_video(request, id):
	Video.objects.get(id=id).delete()
	# vid = Video.objects.get(id=id)
	# print(vid.video_file, vid)
	return redirect(request.META['HTTP_REFERER'])
