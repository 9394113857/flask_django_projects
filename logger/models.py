# logger/models.py

from django.db import models

class Log(models.Model):
    # Fields for your Log model
    route = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.FloatField()

    class Meta:
        db_table = "calculator_logs"  # Set the table name to "calculator_logs"
