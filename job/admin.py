from django.contrib import admin

# Register your models here.
from .models import Category,Job

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'salary', 'posted_at']
    list_filter = ['category', 'location']
    search_fields = ['title', 'company_name', 'location']
    prepopulated_fields = {'slug': ('title',)}