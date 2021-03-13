Приемы по резервному копированию
=================================================

Резервирование базы MySQL


.. code-block:: bash

	#!/bin/bash
	echo "Архивируем дамп"
	myvar=$(mysql -u root damucrm -e "select group_concat(code separator ' ') users from entities where code  not in ('users','table_log_dtls','error_logs','bp_instances','imp_task_rows') and code in (select table_name from information_schema.tables where table_schema=database())")
	if [ $? -eq 0 ]
	then
	  echo "The script ran ok"
	else
	  echo "The script failed" >&2
	  exit 1
	fi
	mysqldump --routines -uroot damucrm $myvar "i\$entity_publish" "i\$increment_version_num" "i\$bp_process_publish" > /opt/backup/gitlab/portal1_test_db/portal1_test_full_current.sql
	echo "Положим в gitlab"
	cd /opt/backup/gitlab/portal1_test_db/
	git add .
	git commit -m "daily autocommit"
	git push origin master
	echo "ok gitlab"
