from django.db import models


# Modèle pour représenter une Catégorie

class Category(models.Model):
    category_title = models.CharField(max_length=100)

    def __str__(self):
        return self.category_title


# Modèle pour représenter un Produit

class Product(models.Model):
    product_title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Assurez-vous d'avoir les paramètres de médias configurés
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title


# Modèle pour représenter une Promotion

class Promotion(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.start_date, self.end_date, self.discount_percentage, self.product
