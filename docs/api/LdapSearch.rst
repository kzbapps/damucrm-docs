LdapSearch - Поиск в LDAP
=================================


.. code-block:: lua

    --Пример:

	output = {}
	
	output.results,output.errText,output.errNum = LdapSearch("domain\\svc.damucrm.webaccess","mypassword","ldaps://ldap-proxy.bapps.kz:636","OU=Accounts,DC=bapps,DC=kz","(objectclass=organizationalPerson)","cn","mail","sAMAccountName")


.. code-block:: json

	{
	  "output": {
		"errNum": 0,
		"errText": "",
		"results": [
		  {
			"cn": "Биапсова Айгерим",
			"mail": "aigerim.ba@bapps.kz",
			"sAMAccountName": "77738144"
		  },
		  {
			"cn": "Бекташева Меруерт",
			"mail": "meruert.b@bapps.kz",
			"sAMAccountName": "77000601"
		  },
		  {
			"cn": "Муратова Жәния",
			"mail": "zhaniya.m@bapps.kz",
			"sAMAccountName": "77000816"
		  }
		  ]
		  }
	}
	  