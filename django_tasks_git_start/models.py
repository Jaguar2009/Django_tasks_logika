from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процесі'),
        ('completed', 'Виконано'),
        ('postponed', 'Відкладено'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
