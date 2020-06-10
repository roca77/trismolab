from django.db import models

# Create your models here.


class Tutor(models.Model):
    skill = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "tutors"

    def __str__(self):
        return self.first_name + " " + self.last_name
