from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MinLengthValidator, MaxLengthValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=50, choices=[
        ('avatar1.png', 'Avatar 1'),
        ('avatar2.png', 'Avatar 2'),
        ('avatar3.png', 'Avatar 3'), 
        ('avatar4.png', 'Avatar 4'),
        ('avatar5.png', 'Avatar 5'),
    ], default='avatar1.png')

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    preview = models.TextField(
        validators=[MinLengthValidator(200), MaxLengthValidator(300)],
        help_text="A short preview of the lesson (200-300 characters)",
    )
    content = CKEditor5Field(null=True, blank=True, config_name='default')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='lessons', blank=True)



    def __str__(self):
        return self.title

# Represents an entire quiz (a collection of questions)
class Quiz(models.Model):
    title = models.CharField(max_length=200, default="Untitled Quiz")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ Link quiz to creator

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
    
