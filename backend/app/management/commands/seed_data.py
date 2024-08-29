from django.core.management.base import BaseCommand
from app.models import Theme, Quiz, Question, Reponse

class Command(BaseCommand):
    help = 'Seed the database with themes, quizzes, and questions'

    def handle(self, *args, **kwargs):
        # Définition des thèmes
        themes = [
            {"name": "Céline Dion", "description": "Questions sur la vie et la carrière de Céline Dion."},
            {"name": "Football", "description": "Questions sur le football."},
            {"name": "Oasis", "description": "Questions sur le groupe Oasis."},
        ]
        
        # Création des thèmes
        for theme_data in themes:
            theme = Theme.objects.create(name=theme_data["name"], description=theme_data["description"])
            
            if theme.name == "Céline Dion":
                # Quiz facile Céline Dion
                quiz1 = Quiz.objects.create(title="Quiz Céline Dion Facile", theme=theme, difficulty='easy')
                self.create_questions(quiz1, [
                    {"content": "Quelle est la date de naissance de Céline Dion ?", 
                     "reponses": ["30 mars 1968", "25 décembre 1970", "1er janvier 1971", "15 août 1970"], 
                     "correct": "30 mars 1968", "multiple_choices": False},
                    {"content": "Quel est le nom du mari de Céline Dion ?", 
                     "reponses": ["René Angélil", "Jean-Jacques Goldman", "Luc Plamondon", "Patrick Bruel"], 
                     "correct": "René Angélil", "multiple_choices": False},
                    # Ajoutez ici d'autres questions...
                ])
                
                # Quiz difficile Céline Dion
                quiz2 = Quiz.objects.create(title="Quiz Céline Dion Difficile", theme=theme, difficulty='hard')
                self.create_questions(quiz2, [
                    {"content": "Combien d'albums a vendu Céline Dion dans le monde ?", 
                     "reponses": ["200 millions", "250 millions", "300 millions", "350 millions"], 
                     "correct": "250 millions", "multiple_choices": True},
                    {"content": "Quel est le nom du premier album en anglais de Céline Dion ?", 
                     "reponses": ["Unison", "Falling into You", "Let's Talk About Love", "The Colour of My Love"], 
                     "correct": "Unison", "multiple_choices": False},
                    # Ajoutez ici d'autres questions...
                ])

            elif theme.name == "Football":
                # Quiz difficile Football
                quiz3 = Quiz.objects.create(title="Quiz Football Difficile", theme=theme, difficulty='hard')
                self.create_questions(quiz3, [
                    {"content": "Quelle équipe a remporté la Coupe du Monde 2018 ?", 
                     "reponses": ["France", "Brésil", "Allemagne", "Argentine"], 
                     "correct": "France", "multiple_choices": True},
                    {"content": "Quel joueur a remporté le Ballon d'Or en 2005 ?", 
                     "reponses": ["Ronaldinho", "Zinédine Zidane", "Cristiano Ronaldo", "Lionel Messi"], 
                     "correct": "Ronaldinho", "multiple_choices": False},
                    # Ajoutez ici d'autres questions...
                ])
            
            elif theme.name == "Oasis":
                # Quiz moyen Oasis
                quiz4 = Quiz.objects.create(title="Quiz Oasis Moyen", theme=theme, difficulty='medium')
                self.create_questions(quiz4, [
                    {"content": "Quel est le nom du premier album du groupe Oasis ?", 
                     "reponses": ["Definitely Maybe", "(What's the Story) Morning Glory?", "Be Here Now", "Heathen Chemistry"], 
                     "correct": "Definitely Maybe", "multiple_choices": False},
                    {"content": "Quel est le titre de la chanson la plus célèbre d'Oasis ?", 
                     "reponses": ["Wonderwall", "Don't Look Back in Anger", "Live Forever", "Champagne Supernova"], 
                     "correct": "Wonderwall", "multiple_choices": True},
                    # Ajoutez ici d'autres questions...
                ])

        self.stdout.write(self.style.SUCCESS('Base de données peuplée avec succès !'))

    def create_questions(self, quiz, questions_data):
        for item in questions_data:
            question = Question.objects.create(
                content=item["content"], 
                quiz=quiz, 
                multiple_choices=item["multiple_choices"]
            )
            for reponse_content in item["reponses"]:
                reponse = Reponse.objects.create(question=question, content=reponse_content)
                if reponse_content == item["correct"]:
                    question.correct_answer = reponse
                    question.save()
