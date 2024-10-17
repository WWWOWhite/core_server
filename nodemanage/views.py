from django.http import JsonResponse
from .models import NodeTable
from .models import LogTable

import datetime, json
from commonutils.utils import *
from django.utils import timezone
import requests
from datetime import datetime



# Create your views here.
def node_update(request):
    if request.method == "POST":
        try:
            # json_data = request.POST.get("update_data")
            # json_data = json.loads(json_data)
            json_data = json.loads(request.body.decode("utf-8"))
            node_id = json_data["node_id"]
            update_instance = NodeTable.objects.get(node_id=node_id)
            if not update_instance:
                return JsonResponse({"status": "error", "message": "node not found"})
            # node_ip = json_data["node_ip"]
            # node_port = int(json_data["node_port"])
            node_desc = json_data["node_desc"]
            # update_instance.node_ip = node_ip
            # update_instance.node_port = node_port
            update_instance.node_desc = node_desc
            update_instance.update_time = timezone.now()
            update_instance.save()
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


def node_add(request):
    if request.method == "POST":
        try:
            # json_data = request.POST.get("add_data")
            # json_data = json.loads(json_data)
            print('node_add')

            json_data = json.loads(request.body.decode("utf-8"))
            node_ip = json_data["node_ip"]
            node_port = int(json_data["node_port"])
            node_desc = json_data["node_desc"]
            print(node_ip,node_port,node_desc)
            node_instance = NodeTable()
            node_instance.node_ip = node_ip
            node_instance.node_port = node_port
            if node_port < 0 or node_port > 65535:
                return JsonResponse({"status": "error", "message": "port out of range"})
            node_instance.node_desc = node_desc
            # node_instance.node_id = calculate_str_hash(node_ip + node_port)
            node_instance.node_is_alive = True
            # node_instance.create_time = time.time().__str__().__format__('YYYY-MM-DD HH:MM')
            node_instance.create_time = datetime.now().strftime('%Y-%m-%d %H:%M')
            node_instance.save()
            print('node_add save')

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


def node_query_all(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode("utf-8"))
            page = json_data["page"]
            limit = json_data["limit"]

            query_instance = NodeTable.objects.all()
            length = query_instance.count()
            if length < page * limit:
                send_instance = query_instance[(page - 1) * limit : length]
            else:
                send_instance = query_instance[(page - 1) * limit : page * limit]

            # TODO 保活机制放到定时任务中

            for temp in send_instance:
                print(temp.get_data())
            data = {
                "num": send_instance.count(),
                "data": [temp.get_data() for temp in send_instance],
            }
            return JsonResponse({"status": "success", "message": data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})




def node_query_by_id(request):
    if request.method == "POST":
        try:
            # json_data = request.POST.get("query_data")
            # json_data = json.loads(json_data)
            json_data = json.loads(request.body.decode("utf-8"))
            node_id = json_data["node_id"]
            node_instance = NodeTable.objects.get(node_id=node_id)
            if not node_instance:
                return JsonResponse({"status": "error", "message": "node not exist"})
            data = node_instance.get_data()
            return JsonResponse({"status": "success", "message": data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


# 同时还需撤销相关注册实体，后续补充
def node_delete(request):
    if request.method == "POST":
        try:
            # json_data = request.POST.get("delete_data")
            # json_data = json.loads(json_data)
            json_data = json.loads(request.body.decode("utf-8"))
            node_id = json_data["node_id"]
            node_instance = NodeTable.objects.get(node_id=node_id)
            if not node_instance:
                return JsonResponse({"status": "error", "message": "node not exist"})
            """
            撤销实体
            """
            node_instance.delete()
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


def node_delete_all():
    NodeTable.objects.all().delete()

def log_delete_all():
    LogTable.objects.all().delete()

def node_load_config(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            json_content = json.loads(data["json_content"])
            # 清空数据库内容
            #   清空节点信息
            node_delete_all()
            #   清空日志信息
            log_delete_all()

            # 将data解析成列表， 将sub和pub的内容用 ，来拼接
            for node in json_content['access_control_list']:
                NodeTable.objects.create(
                    node_id=node['ip'],  # Assuming 'ip' is used as the node_id
                    node_ip=node['ip'],
                    node_port=node['port'],
                    node_sub=",".join(node["subscribe_topic"]),  # Concatenate topics with commas
                    node_pub=",".join(node["publish_topic"]),
                    node_desc=f"Node {node['ip']} - Port {node['port']}",  # Example description
                    node_is_config=False,  # Set this based on your needs
                )
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})


def receive_guid(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            guid = data["guid"]
            topic = data["topic"]
            ip = data["ip"]
            print(guid,topic)

            # 记录日志
            new_log = LogTable.objects.create(
                node_ip=ip,
                log_type='info',  # 日志类型
                log_desc='发布主题: '+topic + '; guid为: '+ guid,  # 日志描述
            )

            # 查询数据库中所有的node , 将topic作为key, ip_port作为value
            #   更优方案, 存储在redis中
            map_topic_ip_port = {}
            query_instance = NodeTable.objects.all()
            for entity in query_instance:
                data = entity.get_data()
                ip_port = data["node_ip"]+":"+str(data["node_port"])
                topics_array = data["node_sub"].split(",")
                for topic_in in topics_array:
                    if topic == topic_in:
                        if topic not in map_topic_ip_port:
                            map_topic_ip_port[topic] = []
                        map_topic_ip_port[topic].append(ip_port)


            # 检索符合订阅条件的节点
            for node in map_topic_ip_port[topic]:
                print(node)
                # 发送配置下发请求
                config_delivery(node,guid)
                # 将guid更新到数据库中
                # 查询数据库对应
                ip = node.split(':')[0]
                node_instance = NodeTable.objects.filter(node_ip=ip).first()
                node_guid = node_instance.white_guid
                print(node_guid)

                if len(node_guid) == 0:
                    # 假设需要对 white_guid 进行某种处理
                    # processed_guid = process_guid(node_guid)  # 替换为实际处理逻辑
                    # print('1')
                    print(f"white_guid 为空，保存新的 guid: {guid}")
                    node_instance.white_guid = guid
                    node_instance.save()
                else:
                    guid_list = node_guid.split(",")  # 将 white_guid 按逗号分割成列表
                    if guid in guid_list:
                        # 如果 guid 已经存在，不做任何操作
                        print(f"guid {guid} 已存在，未修改")
                    else:
                        # 如果 guid 不存在，则追加 guid 并保存
                        new_guid_list = node_guid + ',' + guid
                        print(f"guid {guid} 不存在，更新后的 white_guid: {new_guid_list}")
                        node_instance.white_guid = new_guid_list
                        node_instance.save()

            return JsonResponse({"status": "success"})

        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "message": str(e)})

def process_guid(guid):
    return guid

def config_delivery(ip_port,guid):
    url = 'http://'+ip_port+'/add_guid'
    data = {
        "guid" : guid
    }
    ip = ip_port.split(':')[0]
    response = requests.post(url,json=data)
    json_response = response.json()
    if json_response.get("code") == 200 :
        # 成功
        # 载入数据库
        print("log load",ip)

        # 记录日志
        new_log = LogTable.objects.create(
            node_ip=ip,
            log_type='info',  # 日志类型
            log_desc=json_response.get("msg")  # 日志描述
        )
        print(json_response.get("msg"))
        return
    else:
       #  失败
       new_log = LogTable.objects.create(
           log_node_id=ip,
           log_type='err',  # 日志类型
           log_desc=json_response.get("msg")  # 日志描述
       )
       # 记录日志
       return


def log_query_all(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode("utf-8"))
            page = json_data["page"]
            limit = json_data["limit"]
            ip = json_data["ip"]

            # 通过过滤 node_ip 来查询匹配 IP 的日志
            query_instance = LogTable.objects.filter(node_ip=ip)
            length = query_instance.count()  # 获取匹配的日志条目总数

            if length < page * limit:
                send_instance = query_instance[(page - 1) * limit : length]
            else:
                send_instance = query_instance[(page - 1) * limit : page * limit]

            for temp in send_instance:
                print(temp.get_data())
            data = {
                "num": length,
                "data": [temp.get_data() for temp in send_instance],
            }
            return JsonResponse({"status": "success", "message": data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
