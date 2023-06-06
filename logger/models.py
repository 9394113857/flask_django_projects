from django.db import models

# Create your models here.
class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    route = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()

    def __str__(self):
        return f'{self.timestamp} - {self.route} - {self.operation}'
