from django.contrib import admin
from .models import User, Category, Questions, Stages

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password", "email")

admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "categories")

admin.site.register(Category, CategoryAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("id", "categories", "question", "answer1", "answer2", "answer3", "answer4", "correctanswerchar", "correctanswerint")

admin.site.register(Questions, QuestionsAdmin)

class StagesAdmin(admin.ModelAdmin):
    list_display = ("id", "stage", "description")

admin.site.register(Stages, StagesAdmin)

