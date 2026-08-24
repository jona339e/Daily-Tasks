import uuid
from django.db import models
from django.conf import settings

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    start_time = models.TimeField()
    estimated_duration_minutes = models.PositiveIntegerField(default=15, help_text="Estimated time to complete task in minutes (e.g. 5, 30, 60)")
    actual_duration_minutes = models.PositiveIntegerField(blank=True, null=True, help_text="Actual time spent on task upon completion")
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        indexes = [
            models.Index(fields=['user', 'due_date']),
            models.Index(fields=['user', 'is_completed']),
        ]
        ordering = ['due_date']

    def __str__(self):
        return self.title