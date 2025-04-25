from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class LandingAdminSite(AdminSite):
    site_header = _('Administración de la Landing Page')
    site_title = _('Landing Admin')
    index_title = _('Bienvenido al Panel de Administración de la Landing')

landing_admin_site = LandingAdminSite(name='landing_admin')

