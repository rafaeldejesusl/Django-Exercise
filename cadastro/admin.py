from django.contrib import admin
from cadastro.models import Cliente


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Cliente, Clientes)
