from django.db import models

from course.models import Lesson, BaseModel


class Quiz(BaseModel):

    lesson_quiz = models.OneToOneField(Lesson, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Quizzes"

class Question(BaseModel):

    question_text = models.CharField(max_length=245)
    img_question = models.FileField(null=True, blank=True)
    question_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Choice(BaseModel):

    choice_text = models.CharField(max_length=245)
    is_correct_answer = models.BooleanField(default=False)

    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)