from rest_framework.permissions import IsAuthenticated
from quizapp.models import Category, Question, Quiz, Grade
from .serializers import QuizSerializer, CategorySerializer, QuestionSerializer, GradeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class QuizView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer   
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       category = self.kwargs['category']
       print(category)
       return Quiz.objects.filter(category__name__iexact=category)
    


class QuestionView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        title = self.kwargs['title']
        return Question.objects.filter(quiz__title__iexact=title)

class GradeMVS(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer