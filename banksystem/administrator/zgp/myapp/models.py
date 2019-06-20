from django.db import models

# Create your models here.
class Userinfor(models.Model):
    card_id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    money = models.IntegerField()
    password = models.IntegerField()
    feed = models.IntegerField()
    satime=models.DateField(auto_now=True)
    class Meta:
        db_table = 'userinfor'