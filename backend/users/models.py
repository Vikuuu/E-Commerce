from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.first_name
    
    
class Address(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_zip_code = models.CharField(max_length=9)

    def __str__(self):
        return self.street_address


class PaymentMethod(models.Model):
    PAYMENT_CHOICES = [
        ('CRD', 'CREDIT AND DEBIT CARD'),
        ('UPI', 'UPI'),
        ('COD', 'CASH ON DELIVERY')
    ]
    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=3, choices=PAYMENT_CHOICES)
    
    def __str__(self):
        return self.payment_method


class UserRole(models.Model):
    USER_ROLES = [
        ('C', 'CUSTOMER'),
        ('S', 'SELLER'),
    ]
    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=1, choices=USER_ROLES)
    
    def __str__(self):
        return self.user_role 
