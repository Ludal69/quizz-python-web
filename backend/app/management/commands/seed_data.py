from django.core.management.base import BaseCommand
from app.models import Question, Reponse

class Command(BaseCommand):
    help = 'Peuple la base de données avec des questions sur Céline Dion'

    def handle(self, *args, **kwargs):
        # Liste de questions et réponses
        data = [
            {"question": "Quelle est la date de naissance de Céline Dion ?", "reponses": ["30 mars 1968", "25 décembre 1970", "1er janvier 1971", "15 août 1970"], "correct": "30 mars 1968"},
            {"question": "Quel est le nom du mari de Céline Dion ?", "reponses": ["René Angélil", "Jean-Jacques Goldman", "Luc Plamondon", "Patrick Bruel"], "correct": "René Angélil"},
            # Ajoute 18 autres questions ici...
        ]

        # Ajoute les données dans la base
        for item in data:
            question = Question.objects.create(content=item["question"])
            for reponse_content in item["reponses"]:
                reponse = Reponse.objects.create(question=question, content=reponse_content)
                if reponse_content == item["correct"]:
                    question.correct_answer = reponse
                    question.save()

        self.stdout.write(self.style.SUCCESS('Base de données peuplée avec succès !'))
