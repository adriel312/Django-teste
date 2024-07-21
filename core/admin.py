from django.contrib import admin
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome","preco","estoque")

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)