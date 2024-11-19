from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name