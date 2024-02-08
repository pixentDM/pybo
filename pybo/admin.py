from django.contrib import admin

from pybo.models import Question

class QuestionAdmin(admin.ModelAdmin):          # 제목으로 검색하는 기능
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)