from django.db import models


class Feedback(models.Model):
    feedback_name = models.CharField(max_length=50, verbose_name='Имя покупателя',)
    feedback_email = models.EmailField(verbose_name='Почта покупателя',)
    feedback_message = models.TextField(verbose_name='Текст',)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',)

    class Meta:
        verbose_name = 'Обратная связь покупателя'
        verbose_name_plural = 'Обратная связь покупателя'

    def __str__(self):
        return self.feedback_message[:30]
