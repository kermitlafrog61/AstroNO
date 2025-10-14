from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    registration_start = models.DateTimeField(blank=True)
    registration_end = models.DateTimeField(blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(start_time__lt=models.F(
                "end_time")), name="end_after_start"),
        ]

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.registration_start = self.registration_start or datetime.combine(
            self.date, self.start_time)
        self.registration_end = self.registration_end or datetime.combine(
            self.date, self.end_time)
        return super().save(*args, force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name} ({self.date})'


class Registration(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='registrations')
    student_id = models.CharField(max_length=8)
    student_name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('event', 'student_id')]

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if (timezone.now() < self.event.registration_start
                or timezone.now() > self.event.registration_end):
            raise ValidationError('The event registration is closed')
        return super().save(*args, force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.student_id} ({self.student_name}) - {self.event}'
