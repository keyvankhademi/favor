from django.contrib import admin

# Register your models here.
from .models import ExchangeUser, Token

admin.site.register(ExchangeUser)
admin.site.register(Token)
