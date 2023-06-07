from django.db import models

class Register(models.Model):
    DEPARTMENT_CHOICES = [(1, '1부'), (2, '2부'), (3, '3부')]
    PAID_CHOICES = [('O', '송금했습니다.'), ('X', '아직 송금하지 않았습니다.')]
        
    name = models.CharField(max_length=30)
    department = models.IntegerField(choices=DEPARTMENT_CHOICES)
    phone_number = models.CharField(max_length=13)
    paid = models.CharField(max_length=1, choices=PAID_CHOICES)
    etc = models.TextField()
    registered_at = models.DateTimeField(auto_now_add=True)