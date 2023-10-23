from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Customer models here
DIVISION_CHOICES = (
    ('Chattogram','Chattogram'),
    ('Sylhet', 'Sylhet'),
    ('Rajshahi', 'Rajshahi'),
    ('Khulna', 'Khulna'),
    ('Barishal', 'Barishal'),
    ('Dhaka', 'Dhaka'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    aria = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)



# Product models here
CATEGORY_CHOICES = (
    ('B', 'Baseball'),
    ('F', 'Football'),
    ('C', 'Cricket'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    descriptions = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)




# Cart models here
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)



# OrderPlaced models here
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Picked', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancle', 'Cancle')
)


class OderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')




