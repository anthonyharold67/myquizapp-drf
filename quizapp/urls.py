from django.urls import path
from .views import CategoryView, QuestionView, QuizView,GradeMVS
from rest_framework import routers


router = routers.DefaultRouter()
router.register("grades",GradeMVS)
urlpatterns = [
    path("",CategoryView.as_view()),
    path("quiz/<str:category>/",QuizView.as_view()),
    path("quiz/<str:category>/<str:title>/",QuestionView.as_view()),  
]
urlpatterns += router.urls

