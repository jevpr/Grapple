from django.contrib.auth.models import Group

def user_group_context(request):
    user_group = None
    if request.user.is_authenticated:
        if request.user.groups.filter(name="Content Creators").exists():
            user_group = "Content Creators"
        elif request.user.groups.filter(name="Students").exists():
            user_group = "Students"
    
    return {"user_group": user_group}
