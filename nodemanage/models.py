from Tools.scripts.cleanfuture import verbose
from django.db import models


# Create your models here.
class NodeTable(models.Model):
    node_id = models.CharField(max_length=32, primary_key=True, verbose_name="node id")
    node_ip = models.GenericIPAddressField(verbose_name="node ip")
    node_port = models.IntegerField(verbose_name="node port")
    node_desc = models.TextField(verbose_name="node description", null=True)
    node_is_alive = models.BooleanField(default=True, verbose_name="node alive")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create time")
    update_time = models.DateTimeField(auto_now=True, verbose_name="update time")
    node_sub = models.CharField(max_length=100,verbose_name="node sub")
    node_pub = models.CharField(max_length=100,verbose_name="node pub")
    node_is_config = models.BooleanField(default=True,verbose_name = "node config")
    white_guid = models.TextField(verbose_name="white guid")
    def get_data(self):


        return {
            # "node_id": self.node_id,
            "node_ip": self.node_ip,
            "node_port": self.node_port,
            "node_desc": self.node_desc,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "node_is_alive":self.node_is_alive,
            "node_pub":self.node_pub,
            "node_sub":self.node_sub,
            "white_guid":self.white_guid,
        }


class LogTable(models.Model):
    log_id = models.AutoField(primary_key=True, verbose_name="log id")
    log_type = models.CharField(max_length=20, verbose_name="log type")
    log_desc = models.TextField(verbose_name="log descryption", null=True)
    node_ip = models.CharField(max_length=20, verbose_name="node ip")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create time")
    def get_data(self):
        return {
            # "node_id": self.node_id,
            "log_id": self.log_id,
            "log_type": self.log_type,
            "log_desc": self.log_desc,
            "create_time": self.create_time,
            "node_ip":self.node_ip,
        }