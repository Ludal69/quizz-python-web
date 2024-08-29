from django.http import JsonResponse
from .models import Theme, Quiz

def get_themes(request):
    themes = Theme.objects.all().values('id', 'name')
    return JsonResponse(list(themes), safe=False)

def get_quizzes(request):
    quizzes = Quiz.objects.all().values('id', 'title', 'difficulty', 'theme__name')
    data = [{'id': quiz['id'], 'title': quiz['title'], 'difficulty': quiz['difficulty'], 'category': quiz['theme__name']} for quiz in quizzes]
    return JsonResponse(data, safe=False)
