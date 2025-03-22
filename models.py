from django.db import models

class Attendance(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)  # Auto-stores the current date

    def __str__(self):
        return f"{self.name} - {self.roll_number} - {self.date}"


# Create your models here.
