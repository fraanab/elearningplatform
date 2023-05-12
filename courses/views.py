import json

from core.forms import VideoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import Comment, Course, Orders, UserCourse, Video


def courses(request):
	courses = Course.objects.all()
	allcourses = []													#every course
	for course in courses:
		allcourses.append(course)
	# user_courses = []
	# i = 0    

	if request.user.is_authenticated and not request.user.is_superuser:
		user_courses_id = UserCourse.objects.filter(user=request.user).values_list('course__id', flat=True)
		available_courses = Course.objects.exclude(id__in=user_courses_id)

		user_courses = []
		for user_course in UserCourse.objects.filter(user=request.user):
			user_courses.append(user_course.course)

			# print(user_courses)

		context = {
			'user_courses': user_courses,
			'available_courses': available_courses,
		}
		return render(request, 'courses.html', context)
	else:
		# courses = Course.objects.all()
		return render(request, 'courses.html', {'available_courses':courses})

# @user_passes_test(lambda u: u.is_superuser)
@login_required
def course(request, slug):
	course = Course.objects.get(slug=slug)

	if request.user.is_superuser or UserCourse.objects.filter(user=request.user, course=course):
		comments = Comment.objects.filter(course=course)
		videos = Video.objects.filter(course=course)
		video_form = VideoForm()

		data = {
			'course':course,
			'videos':videos,
			'video_form':video_form,
			'comments':comments
		}
		return render(request, 'view_course.html', data)
	else:
		comments = Comment.objects.filter(course=course)
		videos = Video.objects.filter(course=course)
		videos_list = []
		first_video = None

		for video in videos:
			videos_list.append(video)
			first_video = videos_list[0].video_file.url
			
		data = {
			'course':course,
			'first_video': first_video,
			'comments':comments
		}
		return render(request, 'course.html', data)

@login_required
@require_http_methods(['POST'])
def course_payment(request, id):
	user_pk = request.user
	course_id = Course.objects.get(pk=id)
	order_data = json.loads(request.body)
	id_value = order_data.get('orderID')

	if course_id and id_value:
		Orders.objects.create(order_id=id_value, user=user_pk, course=course_id)
		UserCourse.objects.create(user=user_pk, course=course_id)

		# print(id_value)
		return redirect(request.META['HTTP_REFERER'])
	else:
		raise Http404('Page not found.')

@login_required
@require_http_methods(['POST'])
def create_comment(request, slug):
	course = Course.objects.get(slug=slug)
	message = request.POST.get('message')

	Comment.objects.create(user=request.user, course=course, message=message)
	return redirect(request.META['HTTP_REFERER'])

@login_required
@require_http_methods(['POST'])
def delete_comment(request, id):
	if Comment.objects.filter(user=request.user): 				#if the comment belongs to the authenticated user...
		Comment.objects.get(id=id, user=request.user).delete()  #delete said comment
		return redirect(request.META['HTTP_REFERER']) 			#refresh page
	elif request.user.is_superuser:
		Comment.objects.get(id=id).delete()
		return redirect(request.META['HTTP_REFERER'])
	else:
		raise Http404('There has been a mistake...?')			#if it's a dif user, raising 404
