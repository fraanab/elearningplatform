import uuid

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.text import slugify

media = FileSystemStorage(location="/media/thumbnails")

class Course(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	slug = models.SlugField(blank=True, null=True)
	thumb = models.ImageField(upload_to='courses/thumbnails/', blank=True, null=True)
	# thumb = models.ImageField(storage=media, blank=True, null=True)
	name = models.CharField(max_length=255)
	price = models.IntegerField(default=25)
	description = models.TextField()

	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Course, self).save(*args, **kwargs)

class UserCourse(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} - {self.course.name}'

class Video(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	video_file = models.FileField(upload_to='courses/videos/', blank=True, null=True)
	description = models.TextField()

	def __str__(self):
		return self.name

class Orders(models.Model):
	order_id = models.CharField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user} - {self.order_id} - {self.date} - {self.course}'

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	message = models.TextField(max_length=300)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.course} - {self.user} - {self.message} - {self.date}'
