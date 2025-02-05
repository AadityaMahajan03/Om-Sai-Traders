from django.contrib import admin

from home.models import Employee, Payment, Offer, Stock, Transaction, Sale, Product, Supplier, Category, Customer
# Register your models here.
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Transaction)
admin.site.register(Stock)
admin.site.register(Offer)
admin.site.register(Payment)





