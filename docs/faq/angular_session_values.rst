Значения в сессии
=======================================================================================================================================================

.. code-block:: javascript

    this.sessioninfo.company_id; //ID компании, можно установить, например в значении по умолчанию;
	
.. code-block:: javascript

    this.session_parameters.shortDateFormat; //Параметр, доступен для UI;	
	
.. code-block:: javascript

    this.session_roles.admin; //Роль админа, можно прописать, например в *ngIf="session_roles.admin"