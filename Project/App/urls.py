from django.urls import path
from .views import *


urlpatterns = [
    path("", home_view, name="home_page"),
    path("services/", services_view, name="services_page"),
    path("about/", about_view, name="about_page"),
    path("contact/", contact_view, name="contact_page"),
    # --- Authorization ---
    path("signup/", signup_view, name="signup_page"),
    path("login/", login_view, name="login_page"),
    path("logout/", logout_view, name="logout_page"),
    # --- Authenticate ---
    path("~/", dashboard_overview_view, name="dashboard_overview_page"),
    path("~/activity/", dashboard_activity_view, name="dashboard_activity_page"),
    path("~/usage/", dashboard_usage_view, name="dashboard_usage_page"),
    path("~/settings/", dashboard_settings_view, name="dashboard_settings_page"),
    path("~/notifications/",dashboard_notifications_view,name="dashboard_notifications_page"),
    path("account/", account_settings_view, name="account_page"),
    # --- Account details edit ---
    path("account_details_edit/", account_details_edit_view, name="account_details_edit_page"),

    # --- Delete Account ---
    path("delete/<pk>/", delete_account_view, name="delete_account_page"),
]
