from django.contrib import admin

from .models import TopicTesting, Question, Choice, Answer


class TopicTestingAdmin(admin.ModelAdmin):
    list_display = ('topic_name',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'test_solved', 'question_topic')
    # list_filter = ('TopicTesting',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('wrong_choice', 'right_choice', 'question')
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice', 'created')
    # list_filter = ('user',)


admin.site.register(TopicTesting)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
