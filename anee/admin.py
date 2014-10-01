from mongoadmin import site, DocumentAdmin
from app.models import AppDocument

class AppDocumentAdmin(DocumentAdmin):
    pass
site.register(AppDocument, AppDocumentAdmin)
