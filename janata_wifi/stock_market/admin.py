from django.contrib import admin
from .models import stock_market_model
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StockResource(resources.ModelResource):
   class Meta:
      model = stock_market_model
class StockAdmin(ImportExportModelAdmin):
   resource_class = StockResource

admin.site.register(stock_market_model,StockAdmin)