from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=200, blank=True)  # URL of the image associated with the theme

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    DIFFICULTY_LEVELS = (
        ('easy', 'Facile'),
        ('medium', 'Moyen'),
        ('hard', 'Difficile'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=200, blank=True)  # URL of the image associated with the quiz
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='quizzes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes', default=1)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, default='medium')

    def __str__(self):
        return self.title

    def number_of_questions(self):
        return self.questions.count()

class Question(models.Model):
    content = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', default=1)
    multiple_choices = models.BooleanField(default=True)
    correct_answer = models.ForeignKey('Reponse', on_delete=models.SET_NULL, null=True, related_name='correct_answer_for')

    def __str__(self):
        return self.content

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponses')
    content = models.TextField()

    def __str__(self):
        return self.content
