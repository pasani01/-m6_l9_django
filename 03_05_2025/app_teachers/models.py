from django.db import models

# Create your models here.
class Teacher(models.Model):
    t_fname=models.CharField(max_length=25)
    t_lname=models.CharField(max_length=25)
    t_age=models.IntegerField()
    t_xp_year=models.IntegerField()
    t_email=models.EmailField()
    t_subject=models.CharField(max_length=25)
    class Meta:
        db_table = 'teachers'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'