from django.urls import path
from . import views
from .views import SingleFarm, SingleProduce

urlpatterns = [
    # path('', views.home, name='home'),
    path('farms', views.getFarms, name='farms'),
    path('farm/',
         SingleFarm.as_view(), name='farm'),
    path('add-farm', views.addFarm, name='add-farm'),

    path('produces', views.getProduces, name='produces'),
    path('produce/', SingleProduce.as_view(), name='produce'),
    path('add-produce', views.addProduce, name='add-produce'),
]
