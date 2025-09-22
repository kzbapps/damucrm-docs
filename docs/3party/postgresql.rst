PostgreSQL
===================================================================================

Daily Backup
_____________________________________

.. code-block:: bash

	echo "Архивируем дамп"
	dump=mydb_$(date +"%Y-%m-%d-%H-%M-%S")
	local_dump=/opt/backup/$dump
	#Предварительно подготовьте файл ~/.pgpass (https://www.postgresql.org/docs/9.3/libpq-pgpass.html)
	pg_dump --verbose --host=127.0.0.1 --port=5432 -U mydb --format=c --no-privileges --no-owner --file $local_dump -n "public"
	echo "Резервирование  завершено"	
	
	#Загрузка на SSH Сервер
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
	mkdir $sshserver_dir/files/supervps.bapps.kz/mydb/ -p
	echo "Архивируем ежедневный дамп в sshserver.kz supervps"
	cp -f  $local_dump $sshserver_dir/files/supervps.bapps.kz/mydb/$dump
	echo "Архив mydb выгружен в sshserver.kz supervps!"
	find $sshserver_dir/files/supervps.bapps.kz/mydb/* -mtime +5 -type f -delete
	echo "Удаление старых дампов mydb завершено supervps"	
	umount /mnt/sshserver.kz
	
	#Загрузка на Гугл диск. Подробнее https://medium.com/@enthu.cutlet/how-to-mount-google-drive-on-linux-windows-systems-5ef4bff24288
	echo "google drive"
	google-drive-ocamlfuse /mnt/drive
	cp -f  $local_dump /mnt/drive/backup/mydb/$dump
	find /mnt/drive/backup/mydb/* -mtime +30 -type f -delete
	fusermount -u /mnt/drive
	rm -f $local_dump
