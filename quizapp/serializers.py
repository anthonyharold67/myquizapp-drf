from rest_framework import serializers
from .models import Category, Quiz, Question, Answer, Grade

class CategorySerializer(serializers.ModelSerializer):
    quiz_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id', 'name','quiz_count')

    def get_quiz_count(self, obj):
        return Quiz.objects.filter(category_id=obj.id).count()
    
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text', 'is_right')
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):

    answers=AnswerSerializer(many=True,read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'difficulty','answers')


class QuizSerializer(serializers.ModelSerializer):
    question_count=serializers.SerializerMethodField()
    category=CategorySerializer(read_only=True)
    
    class Meta:
        model = Quiz
        fields = ( 'id','title','question_count','category')
    
    def get_question_count(self,obj):
        return Question.objects.filter(quiz=obj.id).count()

class GradeSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    quiz_id = serializers.IntegerField()
    student = serializers.StringRelatedField()
    student_id = serializers.IntegerField()

    class Meta:
        model = Grade
        fields = ("id","grade","quiz","student","student_id","quiz_id")