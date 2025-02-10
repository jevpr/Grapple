from django.apps import AppConfig


class LearningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learning'


    def ready(self):
        import learning.signals #Import the signals to ensure they are registered


