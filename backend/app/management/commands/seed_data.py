from django.core.management.base import BaseCommand
from app.models import Theme, Quiz, Question, Reponse

class Command(BaseCommand):
    help = 'Peuple la base de données avec deux quizzes sur Céline Dion'

    def handle(self, *args, **kwargs):
        # Créer le thème
        theme_celine = Theme.objects.create(name="Céline Dion", description="Questions sur la vie et la carrière de Céline Dion")

        # Créer les quizzes
        quiz1 = Quiz.objects.create(title="Quiz Céline Dion - 1", theme=theme_celine)
        quiz2 = Quiz.objects.create(title="Quiz Céline Dion - 2", theme=theme_celine)

        # Liste de questions et réponses pour le premier quiz
        questions_quiz1 = [
            {
                "question": "Quelle est la date de naissance de Céline Dion ?",
                "multiple_choices": False,
                "reponses": ["30 mars 1968", "25 décembre 1970", "1er janvier 1971", "15 août 1970"],
                "correct": "30 mars 1968"
            },
            {
                "question": "Quel est le nom du mari de Céline Dion ?",
                "multiple_choices": False,
                "reponses": ["René Angélil", "Jean-Jacques Goldman", "Luc Plamondon", "Patrick Bruel"],
                "correct": "René Angélil"
            },
            {
                "question": "Quel est le titre de la chanson phare du film Titanic interprétée par Céline Dion ?",
                "multiple_choices": True,
                "reponses": ["My Heart Will Go On", "All By Myself", "The Power of Love", "Because You Loved Me"],
                "correct": "My Heart Will Go On"
            },
            # Ajoutez 17 autres questions ici...
        ]

        # Liste de questions et réponses pour le deuxième quiz
        questions_quiz2 = [
            {
                "question": "En quelle année Céline Dion a-t-elle remporté l'Eurovision ?",
                "multiple_choices": True,
                "reponses": ["1988", "1990", "1985", "1992"],
                "correct": "1988"
            },
            {
                "question": "Quel est le titre du premier album anglophone de Céline Dion ?",
                "multiple_choices": True,
                "reponses": ["Unison", "Let's Talk About Love", "Falling Into You", "The Colour of My Love"],
                "correct": "Unison"
            },
            {
                "question": "Combien d'enfants a Céline Dion ?",
                "multiple_choices": False,
                "reponses": ["3", "2", "4", "1"],
                "correct": "3"
            },
            # Ajoutez 17 autres questions ici...
        ]

        # Ajouter les questions et réponses pour le quiz 1
        for item in questions_quiz1:
            question = Question.objects.create(
                content=item["question"],
                quiz=quiz1,
                multiple_choices=item["multiple_choices"]
            )
            for reponse_content in item["reponses"]:
                reponse = Reponse.objects.create(question=question, content=reponse_content)
                if reponse_content == item["correct"]:
                    question.correct_answer = reponse
                    question.save()

        # Ajouter les questions et réponses pour le quiz 2
        for item in questions_quiz2:
            question = Question.objects.create(
                content=item["question"],
                quiz=quiz2,
                multiple_choices=item["multiple_choices"]
            )
            for reponse_content in item["reponses"]:
                reponse = Reponse.objects.create(question=question, content=reponse_content)
                if reponse_content == item["correct"]:
                    question.correct_answer = reponse
                    question.save()

        self.stdout.write(self.style.SUCCESS('Base de données peuplée avec succès !'))
