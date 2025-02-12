from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from .models import Lesson, Quiz, Question, Option, UserProgress, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_image')
    search_fields = ('user__username', 'avatar')
    
    def avatar_image(self, obj):
        avatar_url = static(f'learning/images/{obj.avatar}')
        return format_html(f'<img src="{avatar_url}" style="width: 50px; height: 50px;">')
    

    
    avatar_image.allow_tags = True
    avatar_image.short_description = 'Avatar'

admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserProgress)
admin.site.register(UserProfile, UserProfileAdmin)
    