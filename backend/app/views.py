from django.http import JsonResponse
from .models import Theme, Quiz

def get_themes(request):
    themes = Theme.objects.all().values('id', 'name', 'description', 'image_url')
    return JsonResponse(list(themes), safe=False)

def get_quizzes(request):
    quizzes = Quiz.objects.all().values('id', 'title', 'difficulty', 'theme__name', 'category__name', 'image_url', 'description')
    data = [
        {
            'id': quiz['id'],
            'title': quiz['title'],
            'difficulty': quiz['difficulty'],
            'theme': quiz['theme__name'],
            'category': quiz['category__name'],
            'image_url': quiz['image_url'],   # Add the image URL
            'description': quiz['description']  # Add the description
        }
        for quiz in quizzes
    ]
    return JsonResponse(data, safe=False)

def get_quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all().values('id', 'content', 'multiple_choices', 'correct_answer__id', 'reponses__id', 'reponses__content')
    data = {
        'id': quiz.id,
        'title': quiz.title,
        'description': quiz.description,
        'image_url': quiz.image_url,  
        'number_of_questions': quiz.questions.count(),
        'difficulty': quiz.get_difficulty_display(),
        'category': quiz.category.name,
        'questions': list(questions),
    }
    return JsonResponse(data)
