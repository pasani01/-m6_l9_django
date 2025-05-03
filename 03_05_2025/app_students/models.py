from django.db import models

# Create your models here.
class Students(models.Model):
    s_fullname=models.CharField(max_length=50)
    s_age=models.IntegerField()
    s_grade=models.IntegerField()
    is_active=models.BooleanField()

    class Meta:
        db_table = 'students'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'