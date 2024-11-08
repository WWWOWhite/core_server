from django.urls import path
from . import views

urlpatterns = [
    # 更新节点信息接口
    path("node-update/", views.node_update, name="node-update"),
    # 新增节点接口
    path("node-add/", views.node_add, name="node-add"),
    # 节点查询接口
    path("node-query-all/", views.node_query_all, name="node-query-all"),
    # 删除节点接口
    path("node-delete/", views.node_delete, name="node-delete"),
    # 载入配置接口
    path("node-load-config/",views.node_load_config,name="node-load-config"),
    # 接收节点发送的guid和topic的接口
    path("receive-guid/",views.receive_guid,name="receive-guid"),
    # 查询日志接口
    path("log-query-all/", views.log_query_all, name="log-query-all"),
    # 人为新增白名单接口
    path("add-white/", views.add_white, name="add-white"),
    # 人为删除白名单接口
    path("del-white/", views.del_white, name="del-white"),
]
