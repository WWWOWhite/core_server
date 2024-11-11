# 中心服务器后端代码 
## 环境
- Python 3.10  (3.9也ok)
## 配置修改
进入AS_Server目录下，修改settings.py文件 , 修改和数据库相关的配置。

AS_Server/settings.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 默认
        "NAME": "django_db",  # 连接的数据库  #一定要存在的数据库名
        "HOST": "192.168.19.129",  # mysql的ip地址
        "PORT": 3306,  # mysql的端口
        "USER": "root",  # mysql的用户名
        "PASSWORD": "261619",  # mysql的密码
    }
}
```

## 启动
进入项目根目录

激活python环境
```shell
.\myenv\Scripts\activate
```
启动后端环境
```shell
python3 manage.py runserver 0.0.0.0:8000
```

