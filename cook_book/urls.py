from django.contrib import admin
from django.contrib.auth.models import User, Group
from events.admin import event_admin_site
from django.urls import path

admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Admin Portal"


urlpatterns = [
    path('entity-admin/', admin.site.urls),
    path('event-admin/', event_admin_site.urls),
]
