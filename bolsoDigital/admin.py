from django.contrib import admin
from .models import *

admin.site.register(Expenses)
admin.site.register(Income)
admin.site.register(Category)
# admin.site.register(User)
admin.site.register(Goals)
admin.site.register(AppUser) 


# Register your models here.
