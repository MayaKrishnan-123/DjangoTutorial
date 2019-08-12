from django.contrib import admin

# Register your models here.

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','full_name')
    empty_value_display = 'unknown'


    fieldsets = (
        ('Basic Details', {
            'fields': ('username', 'email', )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('first_name', ),
        }),
    )

    def full_name(self,instance):
        return instance.first_name + " " + instance.last_name


class ExamplelineAdmin(admin.TabularInline):
    model = Example


admin.site.register(User,UserAdmin)
admin.site.register(TestModel)
admin.site.register(Car)
admin.site.register(Example)