from django.apps import AppConfig


class LearningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EnglishLearning.learning'


    def ready(self):
        import EnglishLearning.learning.signals #Import the signals to ensure they are registered


