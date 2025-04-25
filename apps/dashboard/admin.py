from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class DashboardAdminSite(AdminSite):
    site_header = _('Administración del Dashboard')
    site_title = _('Dashboard Admin')
    index_title = _('Bienvenido al Panel de Administración')

dashboard_admin_site = DashboardAdminSite(name='dashboard_admin')
