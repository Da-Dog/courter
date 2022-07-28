from django.urls import re_path
from djangochannelsrestframework.consumers import view_as_consumer
from . import views

websocket_urlpatterns = [
    re_path(r"ws/court/", view_as_consumer(views.CourtView.as_view())),
]
