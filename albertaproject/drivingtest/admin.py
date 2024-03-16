from django.contrib import admin
from .models import Question, Choice

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = Choice
    extra = 4  # Number of extra empty forms

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')
    fieldsets = [
        (None, {'fields': ['text']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
