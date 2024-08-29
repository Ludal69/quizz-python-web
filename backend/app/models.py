from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.title

class Question(models.Model):
    content = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', default=1)  # Remplacez "1" par l'ID de votre quiz par défaut
    multiple_choices = models.BooleanField(default=True)
    correct_answer = models.ForeignKey('Reponse', on_delete=models.SET_NULL, null=True, related_name='correct_answer_for')

    def __str__(self):
        return self.content

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponses')
    content = models.TextField()

    def __str__(self):
        return self.content
