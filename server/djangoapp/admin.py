from django.contrib import admin
from .models import CarMake, CarModel

# Inline admin class for CarModel to be displayed within CarMake's admin page
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms in the inline

# Admin class for CarMake, with CarModel inline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Link CarModel inline with CarMake admin

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'car_make')  # Customize the columns shown in the admin list view
    list_filter = ('type', 'year')  # Add filters in the admin sidebar

# Register the models with their admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
