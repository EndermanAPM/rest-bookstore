from django.db.models import PROTECT, SET_NULL, CASCADE
from django.db import models

# usuarios(id,nombre,edad,fecha_registro,telefono,puntos)
# compras:(id,usuario,libro)
# libros(id,titulo,genero,cantidad,precio,fecha_registro)
# generos(id_genero,nombre)
# stock(id_cantidad,cantidad)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    fidelity_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey(Genre, SET_NULL, null=True)
    available_stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, PROTECT)
    purchase_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id}"


class OrderBookQuantity(models.Model):
    order = models.ForeignKey(Order, CASCADE, "purchased_books")
    book = models.ForeignKey(Book, CASCADE)
    quantity = models.IntegerField()
