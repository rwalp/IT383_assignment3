from django.urls import path
from .views import (
    AssetListView,
    AssetDetailView,
    MaintenanceCreateView,
    export_assets_csv
)

urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('asset/<int:pk>/', AssetDetailView.as_view(), name='asset_detail'),
    path('maintenance/add/', MaintenanceCreateView.as_view(), name='add_maintenance'),
    path('export-csv/', export_assets_csv, name='export_assets_csv'),
]