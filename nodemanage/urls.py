from django.urls import path
from . import views

urlpatterns = [
    path("node-update/", views.node_update, name="node-update"),
    path("node-add/", views.node_add, name="node-add"),
    path("node-query-all/", views.node_query_all, name="node-query-all"),
    path("node-query-by-id/", views.node_query_by_id, name="node-query-by-id"),
    path("node-delete/", views.node_delete, name="node-delete"),
    path("node-load-config/",views.node_load_config,name="node-load-config"),
    path("receive-guid/",views.receive_guid,name="receive-guid"),

    path("log-query-all/", views.log_query_all, name="log-query-all"),
]
