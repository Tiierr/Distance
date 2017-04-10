# 部署

[English version][version-en]

## 在你的 VPS 上部署

### 准备工作

申请[谷歌地图 API Key][google-api-key]并激活。

申请[高德地图 API Key][gaode-api-key]。

### 克隆项目

首先克隆该项目到你的 VPS 上：

```
$ cd /home
$ git clone https://github.com/RayYu03/Distance
```

安装并激活虚拟环境：

```
$ cd Distance
$ python3 -m virtualenv venv
$ source venv/bin/activate
```

安装依赖：

```
(venv) $ pip3 install -r requirements.txt
```

配置 API Key:

```
(venv) $ vim config.py
```

将对应的 key 填入到指定位置:

**GAODE_MAPS_PYTHON_KEY**: 用于后端地理位置编码(国内)。
**GOOGLE_MAPS_PYTHON_KEY**: 用于后端地理位置编码(国际)，需要启用 `Google Maps Geocoding API`。
**GOOGLE_MAPS_JS_KEY**: 用于前端显示地图，需要启用 `Google Maps JavaScript API`。

此外，国内用户还需要将前端 API 的地址修改为国内地址:
```
(venv) $ cd /home/Distance/venv/lib/python3.5/site-packages/flask_googlemaps/templates/googlemaps/
(venv) $ vim gmapjs.html
```

将

```
{%  if not is_googlemaps_loaded()  %}
    {% if GOOGLEMAPS_KEY %}
        <script src="//maps.googleapis.com/maps/api/js?key={{GOOGLEMAPS_KEY}}" type="text/javascript"></script>
    {%  else %}
        <script src="//maps.googleapis.com/maps/api/js" type="text/javascript"></script>
    {%  endif %}
    {{ set_googlemaps_loaded() }}
{% endif %}
```

修改为:

```
{%  if not is_googlemaps_loaded()  %}
    {% if GOOGLEMAPS_KEY %}
        <script src="//maps.google.cn/maps/api/js?key={{GOOGLEMAPS_KEY}}" type="text/javascript"></script>
    {%  else %}
        <script src="//maps.google.cn/maps/api/js" type="text/javascript"></script>
    {%  endif %}
    {{ set_googlemaps_loaded() }}
{% endif %}
```

然后修改地图大小以及缩放比例:

```
(venv) $ cd ..
(venv) $ cd ..
(venv) $ vim __init__.py

set zoom=12
set style="height:550px;width:550px;margin:5px;"

```

测试：

```
(venv) $ python3 manage.py runserver

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger pin code: 165-870-438

```

> 注意: 如果你在本地运行，到这一步就可以了。

### 配置 uwsgi

```
(venv) $ touch config.ini
(venv) $ vim config.ini
```

将以下内容粘贴到里面：

```
[uwsgi]

socket = 127.0.0.1:8001

chdir = /home/Distance

wsgi-file = manage.py

callable = app

processes = 4

threads = 2

stats = 127.0.0.1:9191

```

启动 uwsgi：
```
(venv) $ uwsgi config.ini
```


### 配置 supervisor

安装：

```
(venv) $ pip install supervisor
```

配置`supervisor.conf`：
```
(venv) $ echo_supervisord_conf > /etc/supervisord.conf
(venv) $ vim /etc/supervisord.conf

```

将以下内容粘贴到里面：

```
[program:Distance]

command=/home/Distance/venv/bin/uwsgi /home/Distance/config.ini

directory=/home/Distance

user=root

autostart=true

autorestart=true

stdout_logfile=/home/Distance/logs/uwsgi_supervisor.log
```

启动 supervisor：

```
(venv) $ supervisord -c /etc/supervisord.conf
```

查看 supervisord 是否在运行：

```
ps aux | grep supervisord
```
#### 使用 supervisorctl

Supervisorctl 是 supervisord 的一个命令行客户端工具，启动时需要指定与 supervisord 使用同一份配置文件，否则与 supervisord 一样按照顺序查找配置文件。

```
supervisorctl -c /etc/supervisord.conf
```

上面这个命令会进入 supervisorctl 的 shell 界面，然后可以执行不同的命令了：

```
> status    # 查看程序状态
> stop Distance   # 关闭 Distance 程序
> start Distance  # 启动 Distance 程序
> restart Distance    # 重启 Distance 程序
```


### 配置 nginx

安装：

```
(venv) $ apt-get install nginx
```

配置 default 文件：

```
(venv) $ vim /etc/nginx/sites-available/default
```

将以下内容粘贴到里面：

```
server {
      listen  xx; # 端口号
      server_name xx.xx.xx.xx; # 公网ip

      location / {
        include      uwsgi_params;
        uwsgi_pass   127.0.0.1:8001;

        uwsgi_param UWSGI_PYHOME /home/Distance/venv;

        uwsgi_param UWSGI_CHDIR  /home/Distance;
        uwsgi_param UWSGI_SCRIPT manage:app;
      }
    }
```

重启 nginx ：

```
(venv) $ service nginx restart
```

最后在浏览器地址栏输入公网ip地址和端口号就可以访问了。

[google-api-key]: https://developers.google.com/maps/documentation/javascript/get-api-key

[gaode-api-key]: http://lbs.amap.com/api/javascript-api/summary

[version-en]: https://github.com/RayYu03/Distance/blob/master/deploy.md
