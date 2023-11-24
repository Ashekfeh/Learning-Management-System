from django.db import models
from django.core.validators import RegexValidator

from mptt.models import MPTTModel, TreeForeignKey

from datetime import timedelta
import humanize

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Category(MPTTModel):
    name = models.CharField(max_length=245, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name




class Course(models.Model):
    WEB = 'WD'
    ACC = 'AC'
    DM = 'DM'
    IND = 'ID'


    categories = [
        (WEB, 'web dev'),
        (ACC, 'accounting'),
        (DM, 'digital marketing'),
        (IND, 'Interior Design')
    ]

    ENGLISH = 'EN'
    ARABIC = 'AR'
    FRENCH = 'FR'

    languages = [
        (ENGLISH, 'English'),
        (ARABIC, 'Arabic'),
        (FRENCH, 'French')
    ]


    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=2000, blank=False)
    cover_image = models.FileField()
    duration = models.DurationField(blank=False)
    category = models.OneToOneField(Category, on_delete=models.PROTECT)
    lang = models.CharField(
        max_length=2,
        choices=languages,
        default=ARABIC
    )

    def __str__(self):
        return f'{self.title}, {humanize.precisedelta(self.duration, minimum_unit="minutes")}'


class UserExtension(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    username = models.CharField(max_length=16, blank=False, unique=True, default='deleted_user')
    first_name = models.CharField(max_length=200, blank=False, validators=[alphanumeric])
    last_name = models.CharField(max_length=200, blank=False, validators=[alphanumeric])
    email = models.EmailField(max_length=245)


class Teacher(UserExtension):

    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()} ({self.username})'
    

class Student(UserExtension):

    registered_courses = models.ManyToManyField(Course)
        