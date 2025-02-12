from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

#Do I need a User class here? Is it enough to just import User from django, or do I need to actually 
# need to create a class for it in models.py?


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=50, choices=[
        ('avatar1.svg', 'Avatar 1'),
        ('avatar2.svg', 'Avatar 2'),
        ('avatar3.svg', 'Avatar 3')
    ], default='avatar1.svg')

    def __str__(self):
        return self.user.username



class Lesson (models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Represents an entire quiz (a collection of questions)
class Quiz(models.Model):
    title = models.CharField(max_length=200, default="Untitled Quiz")
    def __str__(self):
        return self.title


# Represents a single question in a quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


# Represents an answer option for a question
class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} - ({'Correct' if self.is_correct else 'Wrong'})"


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.lesson or self.quiz} - Score: {self.score}"
    

