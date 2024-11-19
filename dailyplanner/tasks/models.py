from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Направлена в работу'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнена'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)
    planned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
