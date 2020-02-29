from django.contrib import admin
from .models import Comentario
from .actions import aprova_comentarios, reprova_comentarios


class ComentarioAdmin(admin.ModelAdmin):
    '''
    Esta é uma action personalizada que aparecerá
    na tela do admin. Para aprovar ou rejeitar
    os comentários em massa.
    '''
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comentario, ComentarioAdmin)
