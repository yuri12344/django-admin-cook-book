from django.db.models import Count
from django.contrib import admin
from django import forms
from django.http import HttpResponse
import csv
from .models import *
import ipdb

admin.site.register(Category)
admin.site.register(Villain)

class ExportCsvMixin:
    def export_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = [("name"), ("hero_count"), ("villain_count")]
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        queryset = queryset.annotate(
            _hero_count=Count("hero", distinct=True),
            _villain_count=Count("villain", distinct=True),
        )
        return queryset

    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count

    hero_count.admin_order_field = '_hero_count'
    villain_count.admin_order_field = '_villain_count'


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    actions = ["mark_immortal", "export_csv"]
    
    def is_very_benevolent(self, obj):
        return obj.benevolence_factor > 75
    is_very_benevolent.boolean = True

    def mark_immortal(self, request, queryset):
        queryset.update(is_immortal=True)


    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
        


    class IsVeryBenevolentFilter(admin.SimpleListFilter):
        title = 'is_very_benevolent'
        parameter_name = 'is_very_benevolent'
        
        def lookups(self, request, model_admin):
            return (
                ('Yes', 'Yes'),
                ('No', 'No'),
            )

        def queryset(self, request, queryset):
            value = self.value()
            if value == 'Yes':
                return queryset.filter(benevolence_factor__gt=75)
            elif value == 'No':
                return queryset
            return queryset
            
    list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
    
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
