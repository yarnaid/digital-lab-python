from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

app_name = 'digitallab'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='digitallab/index.html')),
    url(r'^compounds/view-compounds$', views.CompoundView.as_view()),
    url(r'^compounds/edit-compound$', views.edit_compound),
    url(r'^compounds/save-compound$', views.save_compound),
    url(r'^reagents/view-reagents$', views.ReagentsView.as_view()),
    url(r'^reagents/add-reagent$', views.edit_reagents),
    url(r'^reagentlocations/view-reagentlocations$', views.reagent_locations),
    url(r'^reagentlocations/save$', views.reagent_locations),
    url(r'^reagentlocations/add-reagentlocation$', views.edit_reagent_location),
]
