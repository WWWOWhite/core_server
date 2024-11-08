import requests
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
    node_local_white = models.TextField(verbose_name="node local white")
    def get_data(self):

        # sub_topic , pub_topic , guid的值 类型转换成数组
        node_pub_list = self.node_pub.split(',') if self.node_pub else []
        node_sub_list = self.node_sub.split(',') if self.node_sub else []
        white_guid_list = self.white_guid.split(',') if self.white_guid else []
        # TODO 保活机制放到定时任务中
        is_alive,local_guids = query_map_alive(self.node_ip,self.node_port)
        return {
            # "node_id": self.node_id,
            "node_ip": self.node_ip,
            "node_port": self.node_port,
            "node_desc": self.node_desc,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "node_is_alive":is_alive,
            "node_pub": node_pub_list,  # 转换成列表
            "node_sub": node_sub_list,  # 转换成列表
            "white_guid": white_guid_list,  # 转换成列表
            "node_local_white":local_guids,
        }

    def get_data2(self):

        return {
            # "node_id": self.node_id,
            "node_ip": self.node_ip,
            "node_port": self.node_port,
            "node_desc": self.node_desc,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "node_is_alive":self.node_is_alive,
            "node_pub": self.node_pub,
            "node_sub": self.node_sub,
            "white_guid": self.white_guid,
            "node_local_white":self.node_local_white,
        }

def query_map_alive(ip,port):
    url = 'http://'+ip+":"+str(port)+'/query_map'

    try:
        response = requests.get(url,timeout=0.5)
        response.raise_for_status()  # 检查HTTP请求是否成功
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        # 返回空结果并将节点标记为不可用
        update_node_status(ip,0,[])
        return  0,[]

    try:
        json_response = response.json()
    except ValueError:
        print("query_map_alive Error parsing JSON response.")
        # 返回空结果并将节点标记为不可用
        update_node_status(ip, 0,[])
        return 0,[]

    print("query_map success , json content: ", json_response)
    result = []
    if json_response.get("code") == 200 :
        guids = json_response.get("data")
        if len(guids)>0 :
            result = ",".join(guids)
        update_node_status(ip,1,result)
        return 1,guids

    else:
        update_node_status(ip,0,[])
        return 0,[]

def update_node_status(ip,is_alive,guids):
    NodeTable.objects.filter(node_ip=ip).update(node_is_alive=is_alive,node_local_white=guids)

class LogTable(models.Model):
    log_id = models.AutoField(primary_key=True, verbose_name="log id")
    log_type = models.CharField(max_length=20, verbose_name="log type")
    log_desc = models.TextField(verbose_name="log desc", null=True)
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


class GuidTable(models.Model):
    id = models.AutoField(primary_key = True,verbose_name="id")
    guid = models.CharField(max_length=100,verbose_name="guid")
    ip = models.CharField(max_length=100,verbose_name="ip")
    topic = models.CharField(max_length=100,verbose_name="topic")
    def get_data(self):
        return{
            "id":self.id,
            "guid":self.guid,
            "ip":self.ip,
            "topic":self.topic
        }
