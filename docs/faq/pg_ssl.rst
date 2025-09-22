Использование SSL соединения в PostgreSQL
==================================================

1. Сгенерируем сертификаты в папке data:

Вместо localhost укажите название хоста вашей базы

.. code-block:: bash

	openssl genrsa -out root.key 2048
	openssl req -new -x509 -days 365 -key root.key -subj "/C=CN/ST=GD/L=SZ/O=Bapps, Inc./CN=Bapps Root CA" -out root.crt
	openssl req -newkey rsa:2048 -nodes -keyout server.key -subj "/C=CN/ST=GD/L=SZ/O=Bapps, Inc./CN=localhost" -out server.csr
	openssl x509 -req -extfile <(printf "subjectAltName=DNS:localhost") -days 365 -in server.csr -CA root.crt -CAkey root.key -CAcreateserial -out server.crt
	
	
2. Раскомментируем ssl = on в файле postgresql.conf

3. Добавим строку в pg_hba.conf

.. code-block:: text

	hostssl    all             all             127.0.0.1/32         cert

4. Перезапустим базу данных

.. code-block:: bash

	systemctl restart postgresql-server

5. В переменной окружения CRM_DB_CONN_STR прописать sslmode и sslrootcert:

.. code-block:: text

	"CRM_DB_CONN_STR":"postgres://bapps:bapps@localhost:5432/bapps?sslmode=verify-full&TimeZone=Asia/Almaty&sslrootcert=c:\\tmp\\root.crt"

6. Перезапустим приклад

.. code-block:: bash

	systemctl restart damu
