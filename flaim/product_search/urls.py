from django.urls import path

from flaim.product_search.views import IndexView

app_name = "product_search"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

