from django.contrib import admin

from .models import Choice,Question

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  #simple ver
    fieldsets = [
            (None,    {'fields' : ['question_text']}),
            ('Date Information',    {'fields' : ['pub_date']}),
          ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
