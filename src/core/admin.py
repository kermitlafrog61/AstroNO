from django.contrib import admin

from .models import Event, Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["event", "student_name", "status"]
    list_filter = ["status", 'event']
    search_fields = ['student_name', 'student_id']

    def make_published(modeladmin, request, queryset):
        queryset.update(status="c")

    actions = [make_published]

admin.site.register([Event])
