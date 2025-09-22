ITS (Workflow Documents) API 
==================================================================================================

Получить список задач по пользователю
------------------------------------------------------------------------


POST https://damu/restapi/services/run/its_req_get

Либо Authorization: Bearer <token>

Либо Authorization: Basic base64(login:password)

Либо Cookie

Запрос
^^^^^^^^^

.. code-block:: json

	{
		"login":"yeldars",
		"stat_id":3
	}


.. code-block:: text


	"login" - Логин пользователя
	stat_id - Статус заявки

Статусы:

.. code-block:: text

	1 - Создан
	2 - На согласовании
	3 - Закрыта
	4 - Отказана
	5 - На подписании


Ответ
^^^^^^^^^

.. code-block:: json

	{
		"error_code": 0,
		"error_text": "",
		"items": [
			{
				"_executor$": "Молдагулова Алия Нурмухамбетовна",
				"created_at": "2021-06-04 12:41:02",
				"created_by": "1",
				"created_by$": "Молдагулова Алия Нурмухамбетовна",
				"created_by$login": "yeldars",
				"detail_page_url$": "/its/its_hr_kafeteriidetails/55",
				"entity_id": "2028",
				"entity_id$": "Заявка на получение социального пакета по принципу «Кафетерий»",
				"entity_id$code": "its_hr_kafeterii",
				"entity_pk": "55",
				"id": "50",
				"stat_id": "3",
				"stat_id$": "Закрыта",
				"sys$uuid": "d94150a6-077c-42c0-b023-3379eae9fc26",
				"updated_at": "2021-06-04 12:49:15"
			},
			{
				"_executor$": "Молдагулова Алия Нурмухамбетовна",
				"created_at": "2021-06-10 16:21:57",
				"created_by": "1",
				"created_by$": "Молдагулова Алия Нурмухамбетовна",
				"created_by$login": "yeldars",
				"detail_page_url$": "/its/its_hr_premiyadetails/110",
				"entity_id": "2016",
				"entity_id$": "Заявка на премирование сотрудника",
				"entity_id$code": "its_hr_premiya",
				"entity_pk": "110",
				"id": "59",
				"stat_id": "3",
				"stat_id$": "Закрыта",
				"sys$uuid": "eb9bafc4-ac01-4221-82ee-4cbe7bb1843c",
				"updated_at": "2021-06-10 16:26:19"
			}
		]
	}


.. code-block:: text

	"error_code": 0 - Успешный ответ
	_executor$ - Исполнитель - местонахождение
	created_at - Дата создания
	created_by - id Автора
	created_by$ - title Автора
	created_by$login - login Автора
	detail_page_url$ - Страница документа
	entity_id - ID Сущности
	entity_id$ - Title Сущности
	entity_id$code - Код Сущности
	entity_pk - Primary Key записи
	id - Id заявки
	stat_id - ID статуса
	stat_id$ - Title статуса
	sys$uuid$ - UUID заявки
	updated_at - Дата и время обновления заявки


Создать документ
------------------------------------------------------------------------

POST https://damu/restapi/services/run/its_req_create

Либо Authorization: Bearer <token>

Либо Authorization: Basic base64(login:password)

Либо Cookie

Запрос
^^^^^^^^^

.. code-block:: json

	{
		"login": "yeldars",
		"data": [
			{
				"entity_code": "its_hr_premiya",
				"action": "insert",
				"nn": 1,
				"values": {
					"main": {
						"sys$uuid": "fe6d1fdf-0b15-46aa-a12d-fa80aa74f791",
						"dep_id": "1",
						"project_id": "1",
						"reason": "Повышение"
					}
				}
			},
			{
				"entity_code": "its_hr_premiya_user",
				"action": "insert",
				"nn": 2,
				"values": {
					"user1": {
						"user_id": "1",
						"amount": "1000000",
						"its_hr_premiya_id": "fe6d1fdf-0b15-46aa-a12d-fa80aa74f791"
					},
					"user2": {
						"user_id": "2",
						"amount": "1000000",
						"its_hr_premiya_id": "fe6d1fdf-0b15-46aa-a12d-fa80aa74f791"
					}
				}
			}
		]
	}


Ответ
^^^^^^^^^

.. code-block:: json

	{
		"error_code": 0,
		"error_text": "",
		"return": {
			"main": {
				"id": 1,
				"sys$uuid": "fe6d1fdf-0b15-46aa-a12d-fa80aa74f791"
			},
			"user1": {
				"id": 7771,
				"sys$uuid": "fe6d1fdf-0b15-46aa-2222-fa80aa749999"
			},
			"user2": {
				"id": 7772,
				"sys$uuid": "fe6d1fdf-0b15-46aa-7777-fa80aa749999"
			}
		}
	}


Запустить процесс по документу (Отправить)
------------------------------------------------------------------------

POST https://damu/restapi/bpms/start

Либо Authorization: Bearer <token>

Либо Authorization: Basic base64(login:password)

Либо Cookie

Запрос
^^^^^^^^^

.. code-block:: json

	{"processCode":"its_req_premiya","input":{"id":777}}


Ответ
^^^^^^^^^

.. code-block:: json

	{
		"ok":true,
		"instance":"c9e8fb29-7c4a-48af-9204-c5c6211af225",
		"task":"42bcf6de-299f-446f-b4b6-651fb348669d",
		"errorText":"",
		"output":{"last_error":""},
		"instanceIsFinished":false		
	}

Получить список всех доступных действий по документу
------------------------------------------------------------------------

POST https://damu/restapi/services/run/tasks_approves

Либо Authorization: Bearer <token>

Либо Authorization: Basic base64(login:password)

Либо Cookie

Запрос
^^^^^^^^^

.. code-block:: json

	{
		"isNew":false,
		"entity_code":"its_hr_premiya",
		"sys$uuid":"fe6d1fdf-0b15-46aa-a12d-fa80aa74f791"
	}
	
Ответ:
^^^^^^^^^

.. code-block:: json

	{
		"tasks": [
			{
				"approve_t_s_id": "2",
				"can_change_user": "1",
				"due_at": "2021-06-24 02:37:49",
				"id": "2213",
				"is_rq": "1",
				"manager_id": "1",
				"manager_id$title": "Молдагулова Алия Нурмухамбетовна",
				"manager_id$login": "yeldars",
				"status_id$code": "opened",
				"status_id$color": "#85ffc5",
				"status_id$title": "Открыта",
				"step_nn": "1",
				"task_approve_res$": [
					{
						"button_class": "btn btn-primary",
						"do_title": "Согласовать",
						"id": "1",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn btn-danger",
						"do_title": "Отказать",
						"id": "2",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn",
						"do_title": "Переназначить",
						"id": "3",
						"process_code": "task_assign"
					},
					{
						"button_class": "btn btn-primary",
						"do_title": "Согласовать (расширенное)",
						"id": "1",
						"process_code": "task_approve_or_reject_2"
					}
				],
				"title": "Административный руководитель",
				"type_id": "8"
			},
			{
				"approve_t_s_id": "3",
				"can_change_user": "1",
				"due_at": "2021-06-24 02:37:49",
				"id": "2214",
				"is_rq": "1",
				"manager_id": "1",
				"manager_id$title": "Молдагулова Алия Нурмухамбетовна",
				"manager_id$login": "yeldars",
				"status_id$code": "opened",
				"status_id$color": "#85ffc5",
				"status_id$title": "Открыта",
				"step_nn": "1",
				"task_approve_res$": [
					{
						"button_class": "btn btn-primary",
						"do_title": "Согласовать",
						"id": "1",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn btn-danger",
						"do_title": "Отказать",
						"id": "2",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn",
						"do_title": "Переназначить",
						"id": "3",
						"process_code": "task_assign"
					}
				],
				"title": "HR директор/HR менеджер",
				"type_id": "8"
			},
			{
				"approve_t_s_id": "4",
				"can_change_user": "1",
				"due_at": "2021-06-24 02:37:49",
				"id": "2215",
				"is_rq": "1",
				"manager_id": "1",
				"manager_id$title": "Молдагулова Алия Нурмухамбетовна",
				"manager_id$login": "yeldars",
				"status_id$code": "opened",
				"status_id$color": "#85ffc5",
				"status_id$title": "Открыта",
				"step_nn": "1",
				"task_approve_res$": [
					{
						"button_class": "btn btn-primary",
						"do_title": "Согласовать",
						"id": "1",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn btn-danger",
						"do_title": "Отказать",
						"id": "2",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn",
						"do_title": "Переназначить",
						"id": "3",
						"process_code": "task_assign"
					}
				],
				"title": "Финансовый менеджер",
				"type_id": "8"
			},
			{
				"approve_t_s_id": "5",
				"can_change_user": "0",
				"due_at": "2021-06-24 02:37:49",
				"id": "2216",
				"is_rq": "1",
				"manager_id": "1",
				"manager_id$title": "Молдагулова Алия Нурмухамбетовна",
				"manager_id$login": "yeldars",
				"status_id$code": "opened",
				"status_id$color": "#85ffc5",
				"status_id$title": "Открыта",
				"step_nn": "1",
				"task_approve_res$": [
					{
						"button_class": "btn btn-primary",
						"do_title": "Согласовать",
						"id": "1",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn btn-danger",
						"do_title": "Отказать",
						"id": "2",
						"process_code": "task_approve_or_reject"
					},
					{
						"button_class": "btn",
						"do_title": "Переназначить",
						"id": "3",
						"process_code": "task_assign"
					}
				],
				"title": "Дополнительный согласующий",
				"type_id": "8"
			}
		]
	}


Действия доступны в поле task_approve_res$. Проверять доступность действий по полю manager_id$login

В данном примере для документа одному пользователю сразу доступны 4 задачи в которых по три возможных действия (Согласовать,Отказать или Переназначить)


Выполнить действие (Согласовать,Отказать или Переназначить)
----------------------------------------------------------------------

POST https://damu/restapi/bpms/start

Либо Authorization: Bearer <token>

Либо Authorization: Basic base64(login:password)

Либо Cookie

Запрос
^^^^^^^^^

.. code-block:: json

	{
	"processCode":"task_approve_or_reject",
	"input":
		{
		"approve_res_id":"1",
		"step_nn":"1",
		"entity_code":"its_hr_premiya",
		"pk_uuid":"fe6d1fdf-0b15-46aa-a12d-fa80aa74f791"
		}
	}
	
	
Ответ
^^^^^^^^^
.. code-block:: json

	{
		"ok": true,
		"instance": "c4bccb60-da19-4601-96bd-5c6149016c3e",
		"task": "",
		"errorText": "",
		"output": {
			"last_error": ""
		},
		"instanceIsFinished": true
	}	




