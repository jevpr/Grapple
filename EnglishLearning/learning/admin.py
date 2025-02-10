from django.contrib import admin
from .models import Lesson, Quiz, Question, Option, UserProgress

admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserProgress)

    