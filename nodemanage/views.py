import socket

from django.http import JsonResponse
from .models import NodeTable, GuidTable
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
            json_data = json.loads(request.body.decode("utf-8"))
            ip = json_data["node_ip"]
            update_instance = NodeTable.objects.get(node_ip=ip)
            if not update_instance:
                return JsonResponse({"status": "error", "message": "node not found"})

            sub_topic = ','.join(json_data["node_sub"])
            pub_topic = ','.join(json_data["node_pub"])

            # 查询之前的node_sub , 求出两者的差集
            node_instance = NodeTable.objects.get(node_ip=ip)
            data = node_instance.get_data2()
            guid_array = data["node_local_white"].split(",")
            sub_topics_array = data["node_sub"].split(",")
            topic_deleted = []
            now_topic_map = {}

            for topic in json_data["node_sub"]:
                now_topic_map[topic]=1

            for topic in sub_topics_array:
                if topic not in now_topic_map:
                    topic_deleted.append(topic)

            NodeTable.objects.filter(node_ip=ip).update(node_sub=sub_topic, node_pub=pub_topic,update_time=timezone.now())
            print("guid_array : ",guid_array," , topic_deleted : ",topic_deleted)
            # 更新完后再删除，减少并发问题
            if len(topic_deleted) > 0 :
                print("deleted topic array : ", topic_deleted)
                guid_instance = GuidTable.objects.filter(topic__in=topic_deleted, guid__in=guid_array)
                for instance in guid_instance:
                    data = instance.get_data()
                    print("up to delete guid data :",data["guid"])
                    inner_del_white(ip, data["guid"])

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def node_add(request):
    if request.method == "POST":
        try:
            print('node_add')

            json_data = json.loads(request.body.decode("utf-8"))
            node_ip = json_data["node_ip"]
            node_port = int(json_data["node_port"])
            node_desc = json_data["node_desc"]
            node_sub = json_data["node_sub"]
            node_pub = json_data["node_pub"]
            node_sub_str = ','.join(node_sub)
            node_pub_str = ','.join(node_pub)
            print(node_ip,node_port,node_desc)
            node_instance = NodeTable()
            node_instance.node_ip = node_ip
            node_instance.node_port = node_port
            if node_port < 0 or node_port > 65535:
                return JsonResponse({"status": "error", "message": "port out of range"})
            node_instance.node_sub = node_sub_str
            node_instance.node_pub = node_pub_str
            node_instance.node_desc = node_desc
            node_instance.node_is_alive = True
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
            json_data = json.loads(request.body.decode("utf-8"))
            node_ip = json_data["node_ip"]
            node_instance = NodeTable.objects.get(node_ip=node_ip)
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

def guid_delete_all():
    GuidTable.objects.all().delete()

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

            guid_delete_all()
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

# 接收发布节点发送的guid和topic
def receive_guid(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            guid = data["guid"]
            topic = data["topic"]
            ip = data["ip"]


            # 查询数据库中载入的各个节点的访问控制信息,将topic作为key, ip_port作为value
            map_topic_ip_port = {}
            query_instance = NodeTable.objects.all()
            for entity in query_instance:
                data = entity.get_data2()
                ip_port = data["node_ip"]+":"+str(data["node_port"])
                topics_array = data["node_sub"].split(",")
                for topic_in in topics_array:
                    if topic == topic_in:
                        if topic not in map_topic_ip_port:
                            map_topic_ip_port[topic] = []
                        map_topic_ip_port[topic].append(ip_port)
            # 检索符合订阅条件的节点
            for node in map_topic_ip_port[topic]:
                # 将guid更新到数据库中
                ip_suit = node.split(':')[0]
                node_instance = NodeTable.objects.filter(node_ip=ip_suit).first()
                node_guid = node_instance.white_guid
                # 如果节点在线，下发配置
                if node_instance.node_is_alive > 0:
                    config_delivery(node, guid,topic)
                if len(node_guid) == 0:
                    print(f"white_guid 为空，保存新的 guid: {guid}")
                    node_instance.white_guid = guid
                    node_instance.save()
                else:
                    guid_list = node_guid.split(",")
                    if guid in guid_list:
                        print(f"guid {guid} 已存在，未修改")
                    else:
                        new_guid_list = node_guid + ',' + guid
                        print(f"guid {guid} 不存在，更新后的 white_guid: {new_guid_list}")
                        node_instance.white_guid = new_guid_list
                        node_instance.save()

            # 记录guid
            try:
                new_guid = GuidTable.objects.create(
                    ip = ip,
                    topic = topic,
                    guid = guid
                )
            except Exception as e :
                print("the record has existed")

            # 记录日志
            new_log = LogTable.objects.create(
                node_ip=ip,
                log_type='info',  # 日志类型
                log_desc='发布主题: '+topic + '; guid为: '+ guid,  # 日志描述
            )

            return JsonResponse({"status": "success"})

        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "message": str(e)})


# 配置下发
def config_delivery(ip_port,guid,topic):
    url = 'http://'+ip_port+'/add_guid'
    data = {
        "guid" : guid,
        "topic":topic
    }
    ip = ip_port.split(':')[0]
    response = requests.post(url,json=data)
    json_response = response.json()
    # 白名单下发成功
    if json_response.get("code") == 200 :
        print("log load",ip)
        # 记录日志
        if len(topic) > 0 :
            new_log = LogTable.objects.create(
                node_ip=ip,
                log_type='info',  # 日志类型
                log_desc= 'Guid From Topic: \n'+topic+json_response.get("msg")  # 日志描述
            )
            print('Guid From Topic: \n'+topic+json_response.get("msg"))

        else:
            new_log = LogTable.objects.create(
                node_ip=ip,
                log_type='info',  # 日志类型
                log_desc= 'Delete From Core Server \n'+json_response.get("msg")  # 日志描述
            )
            print('Delete From Core Server \n'+json_response.get("msg"))

        return 1,json_response.get("msg")
    # 白名单下发失败
    else:
       #  失败
       new_log = LogTable.objects.create(
           node_ip=ip,
           log_type='err',  # 日志类型
           log_desc=json_response.get("msg")  # 日志描述
       )
       # 记录日志
       print(json_response.get("msg"))
       return 0,json_response.get("msg")

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

            data = {
                "num": length,
                "data": [temp.get_data() for temp in send_instance],
            }
            return JsonResponse({"status": "success", "message": data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def add_white(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode("utf-8"))
            print('add white',json_data)

            ip = json_data["node_ip"]
            guid = json_data["guid"]
            status,msg = config_delivery(ip+':8890',guid,'')
            if status > 0 :
                return JsonResponse({"status": "success","message":msg})
            else:
                return JsonResponse({"err": "error","message":msg})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def del_white(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode("utf-8"))
            ip = json_data["node_ip"]
            guid = json_data["guid"]
            data = {
                "guid":guid,
                "ip" : ip
            }

            url = 'http://' + ip +':8890' + '/delete_guid'
            response = requests.post(url, json=data)
            json_response = response.json()
            if json_response.get("code") == 200:
                # 成功
                # 载入数据库
                print("delete guid log load", ip)
                print(json_response.get("msg"))
                # 记录日志
                new_log = LogTable.objects.create(
                    node_ip=ip,
                    log_type='info',  # 日志类型
                    log_desc=json_response.get("msg")  # 日志描述
                )

                return JsonResponse({"status": "success"})

            else:
                #  失败
                new_log = LogTable.objects.create(
                    node_ip=ip,
                    log_type='err',  # 日志类型
                    log_desc=json_response.get("msg")  # 日志描述
                )
                # 记录日志
                return JsonResponse({"status": "err", "message":json_response.get("msg") })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

def inner_del_white(ip, guid):
    data = {
        "guid": guid,
        "ip": ip
    }
    url = 'http://' + ip + ':8890' + '/delete_guid'
    print("inner del white:", ip, guid)
    try:
        response = requests.post(url, json=data, timeout=0.5)
        json_response = response.json()
        if json_response.get("code") == 200:
            # 成功
            # 载入数据库
            print("update  guid log load", ip)
            # 记录日志
            new_log = LogTable.objects.create(
                node_ip=ip,
                log_type='info',  # 日志类型
                log_desc='With draw guid : ' + guid  # 日志描述
            )
    except Exception as e:
        print("Err : after update withdraw guid failed", e)



def test_add_pub(request):
    print('test_add_pub function is running')
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ip = data["ip"]
            topic = data["topic"]

            pub_message_delivery(ip,topic)
            return JsonResponse({"status": "success"})

        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "message": str(e)})

def pub_message_delivery(pub_ip,topic_name):
    print('pub_message_delivery')
    # 查询所有的ip地址
    node_instances = NodeTable.objects.filter(node_is_alive=1)
    # 对所有ip地址载入字符串加载
    for node in node_instances:
        data = node.get_data()
        ip_log = data['node_ip']
        ip_and_topic = ip_topic_to_16str(pub_ip,topic_name)
        status, msg = add_config(ip_log, ip_and_topic, '')
        if status > 0:
            print(f'节点{ip_log} 成功载入发布端访问控制策略,允许发布端节点 [{pub_ip}] 发布topic [{topic_name}]')
            print(msg)
            new_log = LogTable.objects.create(
                node_ip=ip_log,
                log_type='info',  # 日志类型
                log_desc='成功载入新增发布端控制策略，允许发布端节点 ['+ pub_ip + '] 发布topic ['+ topic_name+']。',  # 日志描述
            )

        else:

            print(f'节点{ip_log} 失败载入发布端访问控制策略')
            print(msg)
            new_log = LogTable.objects.create(
                node_ip=ip_log,
                log_type='err',  # 日志类型
                log_desc='失败载入新增发布端控制策略，发布端节点 ['+ pub_ip + '] 发布topic ['+ topic_name+']。',  # 日志描述
            )

def add_config(ip,str,topic):
    url = 'http://' + ip+':8890' + '/add_guid'
    data = {
        "guid": str,
        "topic": topic
    }
    response = requests.post(url, json=data)
    json_response = response.json()

    if json_response.get("code") == 200:
        return 1, json_response.get("msg")
    else:
        return 0, json_response.get("msg")


def ip_topic_to_16str(ip_str, topic):
    # 将 IP 地址拆分为四个数字，并转换为两位十六进制字符
    ip_hex_chars = ''.join(format(int(part), '02x') for part in ip_str.split('.'))

    # 将 topic 中的每个字符转换为两位十六进制字符
    topic_hex_chars = ''.join(format(ord(char), '02x') for char in topic)

    # 拼接 IP 地址的十六进制和 topic 的十六进制
    result = ip_hex_chars + topic_hex_chars
    return result


