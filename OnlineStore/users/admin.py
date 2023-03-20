from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_name', 'feedback_email',
                    'feedback_message', 'created_at',)
    ordering = ('-created_at',)


admin.site.register(Feedback, FeedbackAdmin)
