from django.db import models


class Contact(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=20)
    Email=models.EmailField(max_length=100)
    Purpose=models.CharField(max_length=50)
    Message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Email
    
