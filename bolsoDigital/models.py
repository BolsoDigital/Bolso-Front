from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'
        
    def __str__(self):
        return self.name


class AppUser(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user'
        
    def __str__(self):
        return self.name or self.email or f"User {self.id}"


class Expenses(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, db_column='id_category', blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='id_user',
        blank=True,
        null=True
    )

    payment_method = models.CharField(max_length=100, blank=True, null=True)
    is_recurring = models.BooleanField(default=False)

    class Meta:
        db_table = 'expenses'
        
    def __str__(self):
        return f"{self.description} - R$ {self.value}"


class Goals(models.Model):
    
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='id_user',
        blank=True,
        null=True
    )

    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, db_column='id_category', blank=True, null=True)
    target_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    period_start = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'goals'
        
    def __str__(self):
        return f"Meta: R$ {self.target_value}"


class Income(models.Model):
    
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='id_user',
        blank=True,
        null=True
    )

    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    received_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'income'
        
    def __str__(self):
        return f"{self.source} - R$ {self.value}"