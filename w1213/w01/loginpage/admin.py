from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'gender', 'mdate')
    search_fields = ('id', 'name', 'mail')  # 검색 필드 추가
    
    
