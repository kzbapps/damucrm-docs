MariaDB
===================================================================================

Daily Backup
_____________________________________

.. code-block:: bash

	echo "Архивируем дамп"
	myvar=$(mysql -u root my_db -e "select group_concat(code separator ' ') users from entities where code  not in ('users','table_log_dtls','error_logs','bp_instances','imp_task_rows') and code in (select table_name from information_schema.tables where table_schema=database())")

	if [ $? -eq 0 ]
	then
	  echo "The script ran ok"
	else
	  echo "The script failed" >&2
	  exit 1
	fi

	echo "Архивируем дамп my_db"

	mysqldump --routines -uroot my_db $myvar "i\$entity_publish" "i\$increment_version_num" "i\$bp_process_publish"  > /opt/backup/my_db.sql


	zip -r /opt/backup/my_db.sql.zip /opt/backup/my_db.sql
	echo "Архивирование в git my_db завершено"
	echo "Положим в gitlab"

	cp /opt/backup/my_db.sql /opt/backup/gitlab/my_db-db/ -r
	cd /opt/backup/gitlab/my_db-db/
	git add .
	git commit -m "daily my_db autocommit"
	git push origin master

	echo "ok gitlab"

	dump=my_db_$(date +"%Y-%m-%d-%H-%M-%S")
	sshserver_dir="/mnt/sshserver.kz"
	umount /mnt/sshserver.kz
	echo "connecting to sshserver"
	#Один раз запустите вручную sshfs чтобы запросил ключи
	if echo 'SSHPASSWORD' | sshfs -o password_stdin sshlogin@sshserver.kz:/ /mnt/sshserver.kz/; then
	echo "ok"
	else
	echo "error on ssh connect sshserver"
	exit
	fi

	mkdir $sshserver_dir/files/supervps.bapps.kz/my_db/ -p
	echo "Архивируем ежедневный дамп в sshserver.kz supervps"
	cp -f  /opt/backup/my_db.sql.zip $sshserver_dir/files/supervps.bapps.kz/my_db/$dump.zip
	echo "Архив my_db выгружен в sshserver.kz supervps!"
	find $sshserver_dir/files/supervps.bapps.kz/my_db/*.zip -mtime +5 -type f -delete
	echo "Удаление старых дампов my_db завершено supervps"
	umount /mnt/sshserver.kz

	#Загрузка на Гугл диск. Подробнее https://medium.com/@enthu.cutlet/how-to-mount-google-drive-on-linux-windows-systems-5ef4bff24288
	echo "google drive"
	google-drive-ocamlfuse /mnt/drive
	cp -f  /opt/backup/my_db.sql.zip /mnt/drive/backup/my_db/$dump.zip
	find /mnt/drive/backup/my_db/*.zip -mtime +30 -type f -delete
	fusermount -u /mnt/drive
