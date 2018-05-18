from django.contrib import admin

# Import your model
from collection.models import Concept

# and setup automated slug creation
class ConceptAdmin(admin.ModelAdmin):
    model = Concept
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register your model
admin.site.register(Concept, ConceptAdmin)
