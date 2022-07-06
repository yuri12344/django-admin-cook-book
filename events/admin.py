from django.contrib import admin
from django.db.models import Count
from .models import *


class EventAdminSite(admin.AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Events Admin Portal"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
        _hero_count=Count("hero", distinct=True),
        _villain_count=Count("villain", distinct=True),
        )
        return queryset

    def hero_count(self, obj):
        return obj.hero_set.count()
    def villain_count(self, obj):
        return obj.villain_set.count()


event_admin_site = admin.AdminSite(name="event_admin")
event_admin_site.register(Epic)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)
event_admin_site.register(Event)

