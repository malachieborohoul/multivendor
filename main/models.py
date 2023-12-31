# ForeignKey
from django.db import models
from django.contrib.auth.models import User
 
#Vendor models
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self) -> str:
        return self.user.username

# ProductCategory
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title
    
# Product
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price= models.FloatField()
    tags = models.TextField(null=True)
    # image  = models.ImageField(upload_to='product_imgs/', null=True)

    

    def __str__(self) -> str:
        return self.title
     
    def tag_list(self):
        tagList = self.tags.split(',')
        return tagList
    
# Customer Model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField(unique=True)
    def __str__(self) -> str:
        return self.user.username
# Order Model

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
       

# OrderItem Model

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.title
    

# Customer Address Model

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_addresses')
    address = models.TextField()
    default_address=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.address
    
# Product Rating and Reviews
class ProductRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='rating_customers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    rating = models.IntegerField()
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.rating} - {self.reviews}'
     

# Product Images Model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image  = models.ImageField(upload_to='product_imgs/')
    

    def __str__(self) -> str:
        return self.image.url