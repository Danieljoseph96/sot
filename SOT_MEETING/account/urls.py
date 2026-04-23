from django.urls import path

from .views import locality_register, locality_register_summary, export_page, export_pdf, export_xlsx, home, import_page, import_xlsx, login_view, logout_view, search, userreg_list

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", home, name="home"),
    path("reg/", locality_register, name="reg"),
    path("reg/summary/", locality_register_summary, name="locality_register_summary"),
    path("userreg/", userreg_list, name="userreg_list"),
    path("search/", search, name="search"),
    path("import/", import_page, name="import_page"),
    path("export/", export_page, name="export_page"),
    path("import/xlsx/", import_xlsx, name="import_xlsx"),
    path("export/xlsx/", export_xlsx, name="export_xlsx"),
    path("export/pdf/", export_pdf, name="export_pdf"),
]
