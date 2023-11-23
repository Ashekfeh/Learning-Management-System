from django.db import models
from datetime import timedelta
import humanize

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
    category = models.CharField(max_length=2, choices=categories, blank=False)
    lang = models.CharField(
        max_length=2,
        choices=languages,
        default=ARABIC
    )

    def __str__(self):
        return f'{self.title}, {humanize.precisedelta(self.duration, minimum_unit="minutes")}'


class UserExtension(models.Model):

    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=245)


class Teacher(UserExtension):

    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
    


