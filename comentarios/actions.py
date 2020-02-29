def reprova_comentarios(model_admin, request, queryset):
    queryset.update(aprovado=False)

def aprova_comentarios(model_admin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentarios.short_description = "Reprovar comentários"
aprova_comentarios.short_description = "Aprovar comentários"
