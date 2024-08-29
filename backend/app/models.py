from django.db import models

class Question(models.Model):
    content = models.TextField()
    correct_answer = models.ForeignKey('Reponse', on_delete=models.SET_NULL, null=True, related_name='correct_answer_for')

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponses')
    content = models.TextField()
