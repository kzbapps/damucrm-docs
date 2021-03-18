SSO, прозрачный вход без пароля
=================================================

1. Создать пользовательскую учетку с неистекающим паролем (krb-icbc)

2. Включить в ней поддержку шифрования Kerberos AES 256 (Галочка This account supports Kerberos AES 256 bit encryption.)

3. Выполнить привязку SPN

.. code-block:: bash

	setspn -A HTTP/bapps.icbc.nb krb-icbc
	
4. Сгенерировать файл

.. code-block:: bash

	ktpass -princ HTTP/bapps.icbc.nb@icbc.com -mapuser krb-icbc -pass 	MY_LITTLE_PASSWORD -crypto all -ptype KRB5_NT_PRINCIPAL -kvno 3 -target bapps.icbc.com -out c:\temp\icbc.keytab

5. Прописать путь к keytab файлу в файле /opt/damucrm/env/damucrm

	Например,
	
.. code-block:: ini
	
	DAMUCRM_KRBKEYTAB_PATH=/opt/k2/env/icbc.keytab
	


