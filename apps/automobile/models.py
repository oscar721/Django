from django.db import models

# Create your models here.

class Brand(models.Model):
    marca=models.CharField(max_length=150, null=False)
    modelo_marca=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField(auto_now=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)
    delete_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.marca

class BrandReference(models.Model):
    reference=models.CharField(max_length=150, null=False)
    brand_id=models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)
    delete_at=models.DateTimeField(null=True)
    def __str__(self):
        return self.reference

class Auto(models.Model):
    brand_id=models.ForeignKey(Brand, on_delete=models.CASCADE)
    reference_id=models.ForeignKey(BrandReference, on_delete=models.CASCADE)
    modelo=models.IntegerField(default=0)
    color=models.CharField(max_length=150, null=False, default="")
    clase=models.CharField(max_length=150, null=False, default="")
    numero_chasis=models.CharField(max_length=150, null=False, default="")
    numero_motor=models.CharField(max_length=150, null=False, default="")
    tipo=models.CharField(max_length=150, null=False, default="")
    placa=models.CharField(max_length=150, null=False, default="")
    kilometraje=models.IntegerField(default=0) 
    cilindraje=models.IntegerField(default=0) 
    tipo_combustible=models.CharField(max_length=150, null=False, default="")
    created_at=models.DateTimeField(auto_now=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)
    delete_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.modelo
