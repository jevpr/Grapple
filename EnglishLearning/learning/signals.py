from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_default_user(sender, instance, created, **kwargs):
    if created: 
        # Get or create the "Students" group
        student_group, _ = Group.objects.get_or_create(name='Students')
        instance.groups.add(student_group)

