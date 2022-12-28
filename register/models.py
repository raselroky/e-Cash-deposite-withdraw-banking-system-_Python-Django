from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.TextField()
    retype_password=models.TextField()
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username
    
