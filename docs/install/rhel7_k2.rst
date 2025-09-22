Установка Приложения DamuCRM с модулем K2 (Картотека обременений №2) на Red Hat Enterprise Linux Server release 7.9 (Maipo)
================================================================================================================================================

1. Установить nginx

.. code-block:: bash

	yum install nginx


2. Установить ghostscript

.. code-block:: bash

	yum install ghostscript


3. Установить libreoffice

.. code-block:: bash

	yum install libreoffice
	

4. Установить дополнительные библиотеки

.. code-block:: bash

	yum install libxml2-devel pcsc-lite libtool-ltdl zip unzip
	
5. Получить дистрибутив и распаковать в /

.. code-block:: bash

	unzip damucrm-k2-pg-distr.zip -d /
	
6. Установить p7zip

.. code-block:: bash

	yum install /opt/p7zip/p7zip-16.02-10.el7.x86_64.rpm	
	
7. Установить pdftk

.. code-block:: bash

	yum install /opt/pdftk/pdftk-2.02-1.el7.x86_64.rpm


8. Включить в автозагрузку К2, Nginx

.. code-block:: bash

	systemctl enable damu
	
	systemctl enable nginx


9. Пропишем настройки соединения с базой данных в файле /opt/damu/env/damu

.. code-block:: bash

	OPENSHIFT_GO_IP=127.0.0.1
	OPENSHIFT_GO_PORT=9999
	OPENSHIFT_APP_NAME=damu
	CRM_DB_CONN_STR=postgres://bapps:************@10.****:5432/bapps?sslmode=disable
	CRM_DB_TYPE=pgsql
	LD_LIBRARY_PATH=:/opt/kalkancrypt/:/opt/kalkancrypt/lib/engines
	DAMUCRM_SALT=SUPERRANDOMSALT
	
	
10. Пропишем настройки nginx в файле /etc/nginx/conf.d/damu.conf

.. code-block:: bash

	#
	# HTTPS server configuration
	#
	  proxy_connect_timeout       6000;
	  proxy_send_timeout          6000;
	  proxy_read_timeout          6000;
	  send_timeout                6000;


	map $http_upgrade $connection_upgrade {
			default upgrade;
			'' close;
	}

	server {
		client_max_body_size 32m;
		server_name  damu.bapps.kz 10.0.0.8;
		root         /usr/share/nginx/html;
		listen 80;
		listen 9060;

		location /static {

			gzip on;
			gzip_disable "msie6";
			gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/javascript;
			root /opt/damu;
		}


		location /restapi/ws {
			#proxy_pass http://websocket;
			proxy_pass http://127.0.0.1:9999;
			proxy_http_version 1.1;
			proxy_set_header Upgrade $http_upgrade;
			#proxy_set_header Connection "upgrade";
			proxy_set_header Connection $connection_upgrade;
			proxy_set_header Origin '';
		}

		location /restapi/list/simple {

			proxy_pass http://127.0.0.1:9999;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $remote_addr;
			proxy_set_header Host $host;
		}

		location / {
			if ($request_uri ~* ".(css|js)(\?v=[0-9.]+)?$") {
				expires 30d;
				access_log off;
				break;
			}

			proxy_pass http://127.0.0.1:9999;

			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $remote_addr;
			proxy_set_header Host $host;

			add_header Last-Modified $date_gmt;
			add_header Cache-Control 'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0';
			if_modified_since off;
			expires off;
			etag off;

			}

	}




11. Примонтируйте сетевую папку для обмена с Fasti, например,

.. code-block:: bash
	
	#cat /etc/rc.d/rc.local
	mount -t cifs -o username=user,password=password,domain=bank.kz,dir_mode=0777,file_mode=0777 //10.0.0.1/share /mnt/fasti/
	
	
12. Запустим k2	


.. code-block:: bash
	
	systemctl start damu
	
	
13. Проверим работоспособность


.. code-block:: bash
	
	systemctl status damu
	
	journalctl -u damu -n 1000
	
В браузере откроем страницу http://10.0.0.8	

