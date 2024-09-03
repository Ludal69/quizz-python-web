from django.core.management.base import BaseCommand
from app.models import Theme, Category, Quiz, Question, Reponse

class Command(BaseCommand):
    help = 'Seed the database with themes, categories, quizzes, and questions'

    def handle(self, *args, **kwargs):
        # Define themes, categories, and image URLs
        themes_categories = {
            "Céline Dion": {
                "description": "Questions sur la vie et la carrière de Céline Dion.",
                "image_url": "/images/celine.png",
                "categories": [
                    {"name": "Musique", "description": "Catégorie pour les quizz musicaux"},
                ]
            },
            "Football": {
                "description": "Questions sur le football.",
                "image_url": "/images/celine.png",
                "categories": [
                    {"name": "Sport", "description": "Catégorie pour les quizz sportifs"},
                    {"name": "Football", "description": "Catégorie spécifique au football"},
                ]
            },
            "Oasis": {
                "description": "Questions sur le groupe Oasis.",
                "image_url": "/images/celine.png",
                "categories": [
                    {"name": "Musique", "description": "Catégorie pour les quizz musicaux"},
                    {"name": "Groupes de Rock", "description": "Catégorie spécifique aux groupes de rock"},
                ]
            },
        }

        # Create themes and categories
        for theme_name, theme_data in themes_categories.items():
            theme = Theme.objects.create(
                name=theme_name, 
                description=theme_data["description"], 
                image_url=theme_data["image_url"]
            )
            
            for category_data in theme_data["categories"]:
                category = Category.objects.create(
                    name=category_data["name"], 
                    description=category_data["description"]
                )
																																			 
					 
					
																									
					
				
	  
                
                # Create quizzes for each category
                if theme.name == "Céline Dion" and category.name == "Musique":
                    # Easy Céline Dion Quiz
                    quiz1 = Quiz.objects.create(
                        title="Quiz Céline Dion Facile", 
                        theme=theme, 
                        category=category, 
                        difficulty='easy',
                        description="Un quiz facile sur la vie et la carrière de Céline Dion.",
                        image_url="/images/celine.png"
                    )
                    self.create_questions(quiz1, [
                        {"content": "Quelle est la date de naissance de Céline Dion ?", 
                         "reponses": ["30 mars 1968", "25 décembre 1970", "1er janvier 1971", "15 août 1970"], 
                         "correct": "30 mars 1968", "multiple_choices": False},
                        {"content": "Quel est le nom du mari de Céline Dion ?", 
                         "reponses": ["René Angélil", "Jean-Jacques Goldman", "Luc Plamondon", "Patrick Bruel"], 
                         "correct": "René Angélil", "multiple_choices": False},
														   
                    ])
                    
                    # Hard Céline Dion Quiz
                    quiz2 = Quiz.objects.create(
                        title="Quiz Céline Dion Difficile", 
                        theme=theme, 
                        category=category, 
                        difficulty='hard',
                        description="Un quiz difficile pour les fans de Céline Dion.",
                        image_url="/images/celine.png"
                    )
                    self.create_questions(quiz2, [
                        {"content": "Combien d'albums a vendu Céline Dion dans le monde ?", 
                         "reponses": ["200 millions", "250 millions", "300 millions", "350 millions"], 
                         "correct": "250 millions", "multiple_choices": True},
                        {"content": "Quel est le nom du premier album en anglais de Céline Dion ?", 
                         "reponses": ["Unison", "Falling into You", "Let's Talk About Love", "The Colour of My Love"], 
                         "correct": "Unison", "multiple_choices": False},
														   
                    ])

                elif theme.name == "Football" and category.name == "Football":
                    # Hard Football Quiz
                    quiz3 = Quiz.objects.create(
                        title="Quiz Football Difficile", 
                        theme=theme, 
                        category=category, 
                        difficulty='hard',
                        description="Un quiz difficile pour les amateurs de football.",
                        image_url="/images/celine.png"
                    )
                    self.create_questions(quiz3, [
                        {"content": "Quelle équipe a remporté la Coupe du Monde 2018 ?", 
                         "reponses": ["France", "Brésil", "Allemagne", "Argentine"], 
                         "correct": "France", "multiple_choices": True},
                        {"content": "Quel joueur a remporté le Ballon d'Or en 2005 ?", 
                         "reponses": ["Ronaldinho", "Zinédine Zidane", "Cristiano Ronaldo", "Lionel Messi"], 
                         "correct": "Ronaldinho", "multiple_choices": False},
														   
                    ])
                
                elif theme.name == "Oasis" and category.name == "Groupes de Rock":
                    # Medium Oasis Quiz
                    quiz4 = Quiz.objects.create(
                        title="Quiz Oasis Moyen", 
                        theme=theme, 
                        category=category, 
                        difficulty='medium',
                        description="Un quiz sur le groupe Oasis pour les amateurs de rock.",
                        image_url="/images/celine.png"
                    )
                    self.create_questions(quiz4, [
                        {"content": "Quel est le nom du premier album du groupe Oasis ?", 
                         "reponses": ["Definitely Maybe", "(What's the Story) Morning Glory?", "Be Here Now", "Heathen Chemistry"], 
                         "correct": "Definitely Maybe", "multiple_choices": False},
                        {"content": "Quel est le titre de la chanson la plus célèbre d'Oasis ?", 
                         "reponses": ["Wonderwall", "Don't Look Back in Anger", "Live Forever", "Champagne Supernova"], 
                         "correct": "Wonderwall", "multiple_choices": True},
														   
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
