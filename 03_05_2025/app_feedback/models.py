from django.db import models

# Create your models here.
class Feedbacks(models.Model):
    f_S_name=models.CharField(max_length=25)
    feedback=models.TextField()
    create_at = models.DateField(auto_now_add=True)