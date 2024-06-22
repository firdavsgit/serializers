from django.contrib import admin

from person.models import Person, Category

admin.site.register(Person)
admin.site.register(Category)
