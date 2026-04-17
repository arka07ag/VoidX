from django.db import models

# Create your models here.



#category model
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



# 5. Product Model 

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    is_sold = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 6. Product Image Model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"    
    



# 10. Banner / Hero Section

class Banner(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.description