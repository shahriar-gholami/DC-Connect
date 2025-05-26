from django.contrib import admin
from .models import *
from django.contrib import messages
from django.utils.html import format_html
from django.urls import reverse

admin.site.site_header = "DC Connect"  # عنوان بالای صفحه (هدر)
admin.site.site_title = "DC Connect"       # عنوان تب مرورگر (title tag)
admin.site.index_title = "DC Connect Management"        # عنوان صفحه اصلی پنل مدیریت

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

@admin.action(description='تعریف سری 24 پورتی برای پچ‌ پنل')
def add_24_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(1,25):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت ۲۴ عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return

@admin.action(description='تعریف سری 48 پورتی برای پچ‌ پنل')
def add_48_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(1,49):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت 48 عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return

@admin.action(description='تعریف سری پورت 1-12 برای پچ‌ پنل')
def add_1_12_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(1,13):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت 12 عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return

@admin.action(description='تعریف سری پورت 13-24 برای پچ‌ پنل')
def add_13_24_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(13,25):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت 12 عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return

@admin.action(description='تعریف سری پورت 25-36 برای پچ‌ پنل')
def add_25_36_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(25,37):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت 12 عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return

@admin.action(description='تعریف سری پورت 37-48 برای پچ‌ پنل')
def add_37_48_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(37,49):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت 12 عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return

@admin.action(description='تعریف سری پورت 25-48 برای پچ‌ پنل')
def add_25_48_ports(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 1:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    print(len(queryset))
    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp = queryset[0]
    for i in range(25,49):
        new_int = Interface.objects.create(
            name = f'{i}',
            device = pp
        )
    modeladmin.message_user(
                request,
                f"گروه پورت 24 عددی به پچ‌پنل اضافه شد.",
                messages.SUCCESS
            )
    return


@admin.action(description='اتصال نظیر به نظیر پچ پنل‌')
def pp_connect(modeladmin, request, queryset):
    # updated = queryset.update(is_active=False)
    if len(queryset) != 2:
        modeladmin.message_user(
        request,
        f"تعداد پچ‌پنل های انتخاب شده باید یک عدد باشد.",
        messages.ERROR
        )
        return

    for device in queryset:
        if device.device_type.title != 'Patch Panel':
            modeladmin.message_user(
                request,
                f"تجهیز انتخاب شده از نوع پچ‌پنل نیست.",
                messages.ERROR
            )
            return
    pp1 = queryset[0]
    pp2 = queryset[1]
    if len(pp1.get_interfaces()) - len(pp2.get_interfaces()):
        modeladmin.message_user(
                request,
                f"تعداد پورت‌های دو تجهیز انتخاب شده یکسان نیست.",
                messages.ERROR
            )
        return

    for j in range(0,min(len(pp2.get_interfaces()),len(pp1.get_interfaces()))):
        new_link = Link.objects.create()
        new_link.terminals.add(pp1.get_interfaces()[j])
        new_link.terminals.add(pp2.get_interfaces()[j])
        new_link.save()

    modeladmin.message_user(
                request,
                f"پورت‌های پچ پنل‌های انتخاب شده نظیر به نظیر متصل شدند.",
                messages.SUCCESS
            )
    return

class InterfaceInline(admin.TabularInline):
    model = Interface
    extra = 0
    can_delete = False
    show_change_link = False  # چون ما لینک را خودمان تولید می‌کنیم
    fields = ['interface_link']
    readonly_fields = ['interface_link']  # جلوگیری از ویرایش

    def interface_link(self, obj):
        if obj.pk:
            url = reverse('admin:info_interface_change', args=[obj.pk])
            return format_html('<a href="{}">{}</a>', url, obj.name)
        return "-"
    interface_link.short_description = "Interface"

    def has_add_permission(self, request, obj=None):
        return False  # جلوگیری از افزودن اینترفیس جدید از این بخش

    def has_change_permission(self, request, obj=None):
        return False  # جلوگیری از تغییر اینترفیس‌ها

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'series', 'rack')
    list_filter = ('device_type', 'rack')
    search_fields = ('name', 'series')
    inlines = [InterfaceInline]
    actions = [pp_connect, add_24_ports, add_48_ports, add_1_12_ports, add_13_24_ports, add_25_36_ports, add_37_48_ports, add_25_48_ports]



@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'get_rack', 'get_row',)
    list_filter = ('device','device__rack', 'device__rack__row')
    search_fields = ('name','device__name')
    fields = ('name', 'device', 'get_pathes_display')  # ترتیب نمایش فیلدها در صفحه ویرایش
    readonly_fields = ('get_pathes_display',)
    autocomplete_fields = ['device',]

    def get_pathes_display(self, obj):
        pathes = obj.get_pathes()  # فرض بر این است که این متد لیستی از اشیاء مدل مسیر برمی‌گرداند
        if len(pathes) == 1:
            path = pathes[0]
            app_label = path._meta.app_label
            model_name = path._meta.model_name
            url = reverse(f'admin:{app_label}_{model_name}_change', args=[path.pk])
            return format_html('<a href="{}">{}</a>', url, str(path))
        return ", ".join(str(p) for p in pathes)

    get_pathes_display.short_description = "Pathes"

    get_pathes_display.short_description = "Path"

    def get_rack(self, obj):
        if obj.device != None:
            return obj.device.rack
        else: return '--'
    get_rack.short_description = 'Rack'

    def get_row(self, obj):
        if obj.device != None:
            return obj.device.rack.row if obj.device and obj.device.rack else None
        else: return '--'
    get_row.short_description = 'Row'


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('get_terminals_display', 'path_position', )
    filter_horizontal = ('terminals',)
    search_fields = ('terminals__name', )


    def get_terminals_display(self, obj):
        return ", ".join(str(t) for t in obj.terminals.all())
    get_terminals_display.short_description = "Terminals"

@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('str_display', 'get_links_count')
    search_fields = ('links',)
    autocomplete_fields = ('links',)
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

    def str_display(self, obj):
        return str(obj)  # همان خروجی __str__
    str_display.short_description = 'Device'  # عنوان ستون




@admin.register(OuterEndPoint)
class OuterEndPointAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['device']