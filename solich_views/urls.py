"""
Solich_views/urls.py
"""

from django.urls import path

from solich_views import views
from solich_views.generic.cbv.views import ReloadMessages

urlpatterns = [
    path("toggle-columns", views.ToggleColumn.as_view(), name="toggle-columns"),
    path("active-tab", views.ActiveTab.as_view(), name="active-tab"),
    path("active-group", views.ActiveGroup.as_view(), name="cbv-active-group"),
    path("reload-field", views.ReloadField.as_view(), name="reload-field"),
    path("reload-messages", ReloadMessages.as_view(), name="reload-messages"),
]

