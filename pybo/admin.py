from django.contrib import admin

# Register your models here.
# 모델을 등록하여서 admin 페이지에서 관리 가능
# subject 검색 기능 추가하기

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question,QuestionAdmin)

