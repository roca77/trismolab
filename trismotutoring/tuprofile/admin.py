from django.contrib import admin

# Register your models here.

from .models import Tutor


class TutorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "skill",)


admin.site.register(Tutor, TutorAdmin)