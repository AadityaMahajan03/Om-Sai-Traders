from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_contact = models.CharField(max_length=20)
    employee_address = models.CharField(max_length=200)
    employee_role = models.CharField(max_length=50)
    employee_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Sale(models.Model):
    sale_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product)  # Add this line to create the many-to-many relationship

    def __str__(self):
        return f"Sale {self.id}"


class Transaction(models.Model):
    transaction_date = models.DateField()
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction {self.id}"


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity} units"


class Offer(models.Model):
    offer_name = models.CharField(max_length=100)
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.offer_name


from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


@receiver(post_save, sender=Sale)
def update_stock_quantity(sender, instance, created, **kwargs):
    if created:
        # Assuming one unit is sold per sale, you may adjust this as needed.
        for product in instance.products.all():
            try:
                # Get the stock entry for the product
                stock = Stock.objects.get(product=product)

                # Calculate the new stock quantity
                new_quantity = stock.quantity - 1

                # Update the stock quantity
                stock.quantity = new_quantity
                stock.save()
            except Stock.DoesNotExist:
                # Handle the case where there is no stock entry for the product
                pass


@receiver(m2m_changed, sender=Sale.products.through)
def update_stock_on_sale_products_changed(sender, instance, action, **kwargs):
    if action == "post_add" or action == "post_remove":
        # Products associated with the sale have changed, so update stock quantities
        for product in instance.products.all():
            try:
                stock = Stock.objects.get(product=product)
                sold_quantity = instance.products.through.objects.filter(product=product, sale=instance).count()
                new_quantity = stock.quantity - sold_quantity
                stock.quantity = new_quantity
                stock.save()
            except Stock.DoesNotExist:
                pass


class Payment(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.sale}"
