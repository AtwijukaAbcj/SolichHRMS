"""
solich_apps

This module is used to register Solich addons
"""

from . import settings
from .settings import INSTALLED_APPS


INSTALLED_APPS.append("biometric")
INSTALLED_APPS.append("solich_audit")
INSTALLED_APPS.append("solich_widgets")
INSTALLED_APPS.append("solich_crumbs")
INSTALLED_APPS.append("solich_documents")
INSTALLED_APPS.append("haystack")
INSTALLED_APPS.append("helpdesk")
INSTALLED_APPS.append("offboarding")
INSTALLED_APPS.append("solich_views")
INSTALLED_APPS.append("solich_automations")
INSTALLED_APPS.append("auditlog")


AUDITLOG_INCLUDE_ALL_MODELS = True

AUDITLOG_EXCLUDE_TRACKING_MODELS = (
    # "<app_name>",
    # "<app_name>.<model>"
)


setattr(
    settings,
    "AUDITLOG_INCLUDE_ALL_MODELS",
    AUDITLOG_INCLUDE_ALL_MODELS,
)

setattr(
    settings,
    "AUDITLOG_EXCLUDE_TRACKING_MODELS",
    AUDITLOG_EXCLUDE_TRACKING_MODELS,
)


settings.MIDDLEWARE.append(
    "auditlog.middleware.AuditlogMiddleware",
)


SETTINGS_EMAIL_BACKEND = getattr(
    settings,
    "EMAIL_BACKEND",
    False,
)

setattr(
    settings,
    "EMAIL_BACKEND",
    "base.backends.ConfiguredEmailBackend",
)

if SETTINGS_EMAIL_BACKEND:
    setattr(
        settings,
        "EMAIL_BACKEND",
        SETTINGS_EMAIL_BACKEND,
    )


SIDEBARS = [
    "recruitment",
    "onboarding",
    "employee",
    "attendance",
    "leave",
    "payroll",
    "pms",
    "offboarding",
    "asset",
    "helpdesk",
]


WHITE_LABELLING = False