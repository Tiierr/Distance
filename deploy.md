# Deploy

[中文版][version-zh]

## Deploy in you VPS

### Preparation

Get a [Google Maps API Key][google-api-key] and activate it.

Get a [Gaode Maps API Key][gaode-api-key].

### Clone the project from github

First of all, please clone the project on your VPS:

```
$ cd /home
$ git clone https://github.com/RayYu03/Distance
```

Install and activate the virtual environment:

```
$ cd Distance
$ python3 -m virtualenv venv
$ source venv/bin/activate
```

Install dependencies:

```
(venv) $ pip3 install -r requirements.txt
```

Configure the API Key:

```
(venv) $ vim config.py
```

Fill the key into the `config.py` file:

- **GAODE_MAPS_PYTHON_KEY**: Gaode Maps API Key
- **GOOGLE_MAPS_PYTHON_KEY**: Google Maps API Key(Activate `Google Maps Geocoding API`)
- **GOOGLE_MAPS_JS_KEY**: Google Maps API Key(Activate `Google Maps JavaScript API`)

Besides, if your VPS IP Address in China, you need change the JavaScript API URL to Chinese version.


```
(venv) $ cd /home/Distance/venv/lib/python3.5/site-packages/flask_googlemaps/templates/googlemaps/
(venv) $ vim gmapjs.html
```

Change the

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

to

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

Then change size and scaling of the Maps.

```
(venv) $ cd ..
(venv) $ cd ..
(venv) $ vim __init__.py

set zoom=12
set style="height:550px;width:550px;margin:5px;"

```

Test:

```
(venv) $ python3 manage.py runserver

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger pin code: 165-870-438

```

> Notice: If you just want to run this project in your local computer, you don't need to read the below steps.

### Configure the uwsgi

```
(venv) $ touch config.ini
(venv) $ vim config.ini
```

Paste the following code into it:

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

Start the uwsgi:

```
(venv) $ uwsgi config.ini
```


### Configure the supervisor

Install:

```
(venv) $ pip install supervisor
```

Configure the `supervisor.conf`:

```
(venv) $ echo_supervisord_conf > /etc/supervisord.conf
(venv) $ vim /etc/supervisord.conf
```

Paste the following code into it:

```
[program:Distance]

command=/home/Distance/venv/bin/uwsgi /home/Distance/config.ini

directory=/home/Distance

user=root

autostart=true

autorestart=true

stdout_logfile=/home/Distance/logs/uwsgi_supervisor.log
```

Start supervisor:

```
(venv) $ supervisord -c /etc/supervisord.conf
```

Confirm the supervisord is running:

```
ps aux | grep supervisord
```

#### Using supervisorctl

The command-line client piece of the supervisor is named supervisorctl. It provides a shell-like interface to the features provided by supervisord. From supervisorctl, a user can connect to different supervisord processes, get status on the subprocesses controlled by, stop and start subprocesses of, and get lists of running processes of a supervisord.

```
supervisorctl -c /etc/supervisord.conf
```

This command will enter into the shell of the supervisorctl. Then you can execute the different command:

```
> status    # check the status of the program
> stop Distance   # close Distance
> start Distance  # start Distance
> restart Distance    # restart Distance
```


### Configure the nginx

Install:

```
(venv) $ apt-get install nginx
```

Configure the default file:

```
(venv) $ vim /etc/nginx/sites-available/default
```

Paste the following code into it:

```
server {
      listen  xx; # Port
      server_name xx.xx.xx.xx; # Public IP Address

      location / {
        include      uwsgi_params;
        uwsgi_pass   127.0.0.1:8001;

        uwsgi_param UWSGI_PYHOME /home/Distance/venv;

        uwsgi_param UWSGI_CHDIR  /home/Distance;
        uwsgi_param UWSGI_SCRIPT manage:app;
      }
    }
```

Change the server_name and port and restart nginx:

```
(venv) $ service nginx restart
```

Input the Public IP Address and port into browser, it's worked.

[google-api-key]: https://developers.google.com/maps/documentation/javascript/get-api-key

[gaode-api-key]: http://lbs.amap.com/api/javascript-api/summary

[version-zh]: https://github.com/RayYu03/Distance/blob/master/deploy.zh.md
