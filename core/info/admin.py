from django.contrib import admin
from .models import *

@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(RackType)
class RackTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'row')
    list_filter = ('type', 'row')
    search_fields = ('name',)

@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device_type', 'series', 'rack')
    list_filter = ('device_type', 'rack')
    search_fields = ('name', 'series')




@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'get_rack', 'get_row', 'get_pathes_display')
    list_filter = ('device','device__rack', 'device__rack__row')
    search_fields = ('name','device__name')

    def get_pathes_display(self, obj):
        pathes = obj.get_pathes()
        return ", ".join(str(t) for t in pathes)

    get_pathes_display.short_description = "Path"

    def get_rack(self, obj):
        return obj.device.rack
    get_rack.short_description = 'Rack'

    def get_row(self, obj):
        return obj.device.rack.row if obj.device and obj.device.rack else None
    get_row.short_description = 'Row'


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'path_position', 'get_terminals_display')
    filter_horizontal = ('terminals',)
    search_fields = ('terminals__name', )

    def get_terminals_display(self, obj):
        return ", ".join(str(t) for t in obj.terminals.all())
    get_terminals_display.short_description = "Terminals"

@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_links_count', 'get_terminals_display')
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.sort_links_by_path_order()
        return super().change_view(request, object_id, form_url, extra_context)

    def get_links_count(self, obj):
        return obj.links.count()
    get_links_count.short_description = "Links Count"

    def get_terminals_display(self, obj):
        terminals = obj.get_terminals()
        return ", ".join(str(t) for t in terminals)
    get_terminals_display.short_description = "Terminals"