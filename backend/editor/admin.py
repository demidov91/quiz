from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableStackedInline

from editor.models import Quiz, Question, Answer



class QuizAdmin(SortableAdmin):
    list_display = 'name',


class AnswerAdminInline(SortableStackedInline):
    extra = 0
    model = Answer


class QuestionAdmin(SortableAdmin):
    list_filter = 'quiz',
    list_display = 'text', 'quiz'
    inlines = AnswerAdminInline,


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
