from django.contrib import admin

from .models import Messages, ConversationMessage
# Register your models here.
admin.site.register(Messages)
admin.site.register(ConversationMessage)