from django.contrib import admin

from .models import Course
from .models import Teacher
from .models import Student
from .models import Category

from mptt.admin import DraggableMPTTAdmin

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),
)