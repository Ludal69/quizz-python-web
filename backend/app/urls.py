from django.urls import path
from .views import get_themes, get_quizzes

urlpatterns = [
    path('api/themes/', get_themes),  # Route pour les thématiques
    path('api/quizzes/', get_quizzes),  # Route pour les quiz
]
