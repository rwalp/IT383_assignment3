from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
import csv

from .models import Asset, MaintenanceLog

class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'
    paginate_by = 5  


class AssetDetailView(DetailView):
    model = Asset
    template_name = 'asset_detail.html'
    context_object_name = 'asset'


class MaintenanceCreateView(CreateView):
    model = MaintenanceLog
    fields = ['asset', 'service_date', 'description', 'cost']
    template_name = 'maintenance_form.html'

    def get_success_url(self):
        return reverse_lazy('asset_detail', kwargs={'pk': self.object.asset.id})



def export_assets_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="asset_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Asset Name', 'Type', 'Cost', 'Assigned User'])

    assets = Asset.objects.all()

    for asset in assets:
        writer.writerow([
            asset.name,
            asset.asset_type,
            asset.cost,
            asset.assigned_user
        ])

    return response 