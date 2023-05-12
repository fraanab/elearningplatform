from django.contrib import admin

from .models import Course, Orders, UserCourse, Video

admin.site.register(Course)
admin.site.register(UserCourse)
admin.site.register(Video)
admin.site.register(Orders)
