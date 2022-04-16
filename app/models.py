from django.db import models

# Create your models here.

CHOICES = (
	("1", "Available"),
	("2", "Not Available")
)

class Brand(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name

class Product(models.Model):
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	name = models.CharField(max_length=255)
	code = models.CharField(max_length=10)
	image = models.ImageField(upload_to="media/product/images/")
	quantity = models.IntegerField()
	rate = models.FloatField(max_length=100)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name

class Order(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	sub_total = models.FloatField(max_length=100)
	vat = models.FloatField(max_length=100)
	total_amount = models.FloatField(max_length=100)
	discount = models.FloatField(max_length=100)
	grand_total = models.FloatField(max_length=100)
	paid = models.FloatField(max_length=100)
	due = models.FloatField(max_length=100)
	payment_type = models.CharField(max_length=100)
	payment_status = models.IntegerField()
	status = models.IntegerField()

class OrderItem(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

	quantity = models.IntegerField()
	rate = models.FloatField(max_length=100)
	total = models.FloatField(max_length=100)
	status = models.IntegerField()












