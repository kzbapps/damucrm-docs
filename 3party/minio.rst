Min.io Администрирование
===================================================================================

Установка min.io Клиент
_____________________________________

.. code-block:: bash

	wget https://dl.min.io/client/mc/release/linux-amd64/mc
	cp mc /usr/bin/m-c
	chmod +x /usr/bin/m-c
	m-c alias set localhost http://localhost:39199 "login" "password"
	m-c admin policy list localhost
	m-c admin user add localhost
	m-c mb localhost/someclient

Установка доступа
_____________________________________

Создадим файл someclient.policy

.. code-block:: text

	{
	  "Version": "2022-07-26",
	  "Statement": [
		{
		  "Action": [
			"s3:PutBucketPolicy",
			"s3:GetBucketPolicy",
			"s3:DeleteBucketPolicy",
			"s3:ListAllMyBuckets",
			"s3:ListBucket"
		  ],
		  "Effect": "Allow",
		  "Resource": [
			"arn:aws:s3:::someclient"
		  ],
		  "Sid": ""
		},
		{
		  "Action": [
			"s3:AbortMultipartUpload",
			"s3:DeleteObject",
			"s3:GetObject",
			"s3:ListMultipartUploadParts",
			"s3:PutObject"
		  ],
		  "Effect": "Allow",
		  "Resource": [
			"arn:aws:s3:::someclient/*"
		  ],
		  "Sid": ""
		}
	  ]
	}

.. code-block:: bash

	m-c admin policy add localhost someclient-policy someclient.policy
	m-c admin policy set localhost someclient-policy user=someclient



Резервное копирование на сервер
_____________________________________

Пропишем алиас

.. code-block:: text

	m-c alias set somevendor  http://somevendor.example.com:39199 "someclientlogin" "someclientpassword"

Создадим Файл ~/.pgpass

.. code-block:: text

	hostname:port:database:username:password

.. code-block:: bash

	#!/bin/bash
	dump=someclient_test_$(date +"%Y-%m-%d-%H-%M-%S")
	local_dump=/home/someclient_user/$dump
	pg_dump --verbose --host=127.0.0.1 --port=5432 -U someclient_test --format=c --no-privileges --no-owner --file $local_dump

	m-c cp $local_dump somevendor/someclient_test/dumps/

	m-c rm --force --older-than 10d somevendor/someclient_bucket/dumps/

Добавим в планировщик /etc/crontab

.. code-block:: text

	0 2 * * * someclient_user /opt/damu/scripts/create_backup_to_vendor.sh
	

