from django.urls import path
from core.views import (index, labelCreateView, labelUpdateView)

urlpatterns = [
    path('index/', index, name= "index"),
    path('list_label/', labelCreateView.as_view(), name= "list_label"),
    path('add_label/', labelCreateView.as_view(), name= "add_label"),
    path('update_label/<int:pk>', labelUpdateView.as_view(), name= "update_label"),
]
