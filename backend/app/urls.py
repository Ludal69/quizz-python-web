from django.urls import path
from .views import get_themes, get_quizzes
from .views import get_quiz_detail

urlpatterns = [
    path('api/themes/', get_themes),  # Route pour les thématiques
    path('api/quizzes/', get_quizzes),  # Route pour les quiz
    path('api/quiz/<int:quiz_id>/', get_quiz_detail),
]
