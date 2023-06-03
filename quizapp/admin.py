from django.contrib import admin
import nested_admin
from .models import Quiz, Category, Question, Answer,Grade


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer



class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
   
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines= [QuestionInline]


admin.site.register(Quiz,QuizAdmin)

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Grade)