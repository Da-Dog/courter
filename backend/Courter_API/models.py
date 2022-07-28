from django.db import models


# Create your models here.
class Court(models.Model):
    number = models.IntegerField(unique=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    rental_status = models.BooleanField(default=False)
    rental_start_time = models.DateTimeField(null=True, blank=True)
    rental_end_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=64)
    logged_in = models.BooleanField(default=False)
    current_court = models.ForeignKey(Court, on_delete=models.CASCADE, null=True, related_name='current_court')
    waiting_court = models.ForeignKey(Court, on_delete=models.CASCADE, null=True, related_name='waiting_court')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
