from django.db import models

class Feedback(models.Model):
    feedback_name = models.CharField(max_length=50)
    feedback_email = models.EmailField()
    feedback_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_message[:30]
    