from django.db import models

class Bank(models.Model):
	acno=models.IntegerField()
	name=models.CharField(max_length=64)
	depamnt=models.IntegerField()
	bal=models.IntegerField()
