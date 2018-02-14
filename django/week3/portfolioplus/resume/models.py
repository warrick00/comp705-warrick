from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=64, null=False, blank=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    start_date = models.DateField(max_length=255, null=False, blank=True)
    end_date = models.DateField(max_length=355, null=False, blank=True)
    description = models.TextField(max_length=255, null=False, blank=True)

    def new_experience(self):
        return self.new_experience

class Education(models.Model):
    institution_name = models.CharField(max_length=64, null=False, blank=True)
    location = models.CharField(max_length=255, null=False, blank=True)
    degree = models.CharField(max_length=255, null=False, blank=True)
    major = models.CharField(max_length=355, null=False, blank=True)
    gpa = models.FloatField()

    def new_education(self):
        return self.new_education
