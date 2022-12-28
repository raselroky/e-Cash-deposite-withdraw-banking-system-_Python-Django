from django.db import models


class E_cash(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=1000)
    deposite_withdraw=models.TextField()
    amount=models.TextField()
    total_amount=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username +' '+ str(self.id)
    

