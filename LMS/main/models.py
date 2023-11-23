from django.db import models

class Course(models.Model):
    categories = [
        (1, 'web dev'),
        (2, 'accounting'),
        (3, 'digital marketing'),
        (4, 'Interior Design')
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
    duration = models.TimeField(blank=False)
    category = models.CharField(max_length=2, choices=categories, blank=False)
    lang = models.CharField(
        max_length=2,
        choices=languages,
        default=ARABIC
    )
