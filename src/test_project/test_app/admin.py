from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline

from reversion.admin import VersionAdmin


from test_project.test_app.models import ChildModel, ParentModel, RelatedModel, GenericRelatedModel, ProxyModel


class RelatedModelInline(admin.StackedInline):
    
    model = RelatedModel
    
    
class GenericRelatedInline(GenericStackedInline):
    
    model = GenericRelatedModel
    
    
class ChildModelAdmin(VersionAdmin):
    
    inlines = RelatedModelInline, GenericRelatedInline,
    
    
admin.site.register(ChildModel, ChildModelAdmin)


admin.site.register(ProxyModel, ChildModelAdmin)

