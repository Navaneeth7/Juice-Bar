from django.db import models
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class Categories(models.Model):
    image=models.ImageField(upload_to='static/images/')
    heading=models.CharField(max_length=40)
    descrption=models.CharField(max_length=300,null=True)
    product1=models.CharField(max_length=100,null=True)
    product2=models.CharField(max_length=100,null=True)
    product3=models.CharField(max_length=100,null=True)
    product4=models.CharField(max_length=100,null=True)
    product5=models.CharField(max_length=100,null=True)
    product6=models.CharField(max_length=100,null=True)
    product7=models.CharField(max_length=100,null=True)
    product8=models.CharField(max_length=100,null=True)
    product9=models.CharField(max_length=100,null=True)
    product10=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.heading

class products(models.Model):
    image=models.ImageField(upload_to='static/images/')
    productName=models.CharField(max_length=50)
    productPrice=models.IntegerField(null=True)
    quantity=models.CharField(null=True,max_length=30)
    Discount=models.IntegerField(default=0)
    Category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.productName


from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return self.username
    
class cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField(default=0)
    number=models.IntegerField(null=True,default=1)
    
class Orders(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email} - {self.product.productName}"

    def send_order_email(self):
        subject = "New Order Placed"
        message = f"""
        A new order has been placed!
        Username:{self.user.username}
        Email:{self.user.email}
        Product: {self.product.productName}
        Quantity: {self.quantity}
        Price: ₹{self.price}
        Ordered At: {self.ordered_at.strftime('%Y-%m-%d %H:%M:%S')}
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['juicebarhq@gmail.com'],
            fail_silently=False,
        )

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Check if this is a new order
        super().save(*args, **kwargs)
        if is_new:
            self.send_order_email()
