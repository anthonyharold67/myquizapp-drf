
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categories')
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='quizzes')
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField(default=1,choices=[(1,"Easy"),(2,"Medium"),(3,"Hard")])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    answer_text = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_text
class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Username : {self.student.username} - Score : {self.grade}"
  
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'quiz'], name='unique_student_quiz')
        ]