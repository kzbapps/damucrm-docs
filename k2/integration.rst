Описание интеграции
==================================================================================================

Данный раздел описывает интеграции с системой Картотека обременений(К2)

Сервисы для приема
---------------------------

Сервис приема сведений о просроченной задолженности
_______________________________________________________________

Запрос

.. code-block:: text

	POST https://{$k2host}/restapi/services/run/k2loan_from_eko


.. code-block:: text

     [
          {
		    "request_id": 1111,
			"iban": "KZ000000000000000000",
			"cur": "KZT",
			"debt": 2000000,
			"fullname": "Тестовый Тест Тестович",
			"contract_number": "KD0000000001",
			"dbz_contract_number": "KD0000000001",
			"dbz_dt": "2014-02-08",
			"dep_id": 555,
			"id": 666,
			"problemfl": 1, /*признак проблемности – тип : число*/
			"segment": "01", /*Сегмент бизнеса – тип : строка(20)*/
			"dea_dord:"2021-01-01" /*дата оформления линии */
			"dea_dep_id": 777,/*линия.id */
			"dea_id": 888, /*линия.dep_id */
			"dea_code": 999, /*линия.code */

			"iinbin": "000000000000",
			"overdue_days": 90,
			"system": "way4"
          }
          ,
          {

          }
          ,
          {

          }
     ]


Успешный Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }

"error_code":0 - успешный ответ

Неуспешный Ответ:

.. code-block:: json

	{
		"error_code": 13,
		"error_text": "Неверная длина ИИН",
		"errors": [
			{
				"error_code": 15,
				"error_text": "Неверная длина ИИН",
				"request_id": 111
			},
			{
				"error_code": 15,
				"error_text": "Неверная длина ИИН",
				"request_id": 1112
			}
		]
	}


Сервис приема платежей по исходящим платежным требованиям
_______________________________________________________________

Запрос

.. code-block:: text

	POST https://{$k2host}/restapi/services/run/k2extreq_pay_from_eko


.. code-block:: json

	{
		"items":
		 [
			  {
				"request_id": 1111,
				"trn_id": 11111111,
				"refer": "PTPJ200000000037",
				"cur": "KZT",
				"amount": 2000000,
				"incoming_amount":3000000
			  },
			  {
				"request_id": 1112,
				"trn_id": 11111112,
				"refer": "PTPJ200000000037",
				"cur": "KZT",
				"amount": 3000000,
				"incoming_amount": 3000000
			  }
		 ]
	}

.. list-table:: Описание полей
     :header-rows: 1

     * - Поле
       - Описание
     * - request_id
       - Уникальный номер запроса
     * - trn_id
       - Уникальный ID транзакции из АБС
     * - refer
       - Референс исходящего платежного требования
     * - cur
       - Валюта
     * - amount
       - Cумма платежа
     * - incoming_amount
       - Cумма поступления

Успешный Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }

"error_code":0 - успешный ответ

Неуспешный Ответ:

.. code-block:: json

	{
		"error_code": 1,
		"error_text": "Обнаружены ошибки при приеме платежей",
		"errors": [
			{
				"error_code": 9,
				"error_text": "pq: duplicate key value violates unique constraint \"k2extreq_pay_trn_id_uindex\"",
				"request_id": 1111
			}
		]
	}



Сервис актуализации информации о долге
_______________________________________________________________

Запрос

.. code-block:: text

	POST https://{$k2host}/restapi/services/run/k2loan_sync_debt


.. code-block:: json

     [
          {
			"debt": 2000000,
			"contract_number": "KD0000000001"
          }
          ,
          {

          }
          ,
          {

          }
     ]


Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }



"error_code":0 - успешный ответ


Сервис получения информации о исходящих платежных поручениях по Дате и номеру ДБЗ
______________________________________________________________________________________________________________________________

POST https://{$k2host}/restapi/services/run/k2extreq_by_dbz

.. code-block:: json

     {
          "contract_number": "KD0000000001",
          "dbz_dt": "2021-01-01"
     }


.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - contract_number
     - Номер ДБЗ
   * - dbz_dt
     - Дата ДБЗ

Ответ:

.. code-block:: text

	{
		"error_code":0,
		"error_text":"",
		"items": [
			{
				"amount": "10001.00", /* Сумма ПТ*/
				"bank_code": "KPSTKZKA", /* Банк*/
				"bank_id": "18",
				"bank_id$": "АО \"Рога и копыта\"", /* Наименование Банка*/
				"bank_id$header_paper": "Председателю Правления <br />\nАО «Рога И копыта»  <br />\nгосподину Гансу Христиану Андерсону", /* Обращение Руководителю Банка*/
				"cli_id": "1639",
				"cli_id$": "ФИО Клиента", /* ФИО Клиента*/
				"cli_iin": "000000000000", /* ИИН Клиента*/
				"code": "PTPJMIG0000003817", /* Референс ПТ */
				"created_at": "2021-10-20T18:21:24.240319+06:00", /* Дата создания ПТ*/
				"created_at_fmt": "20.10.2021", /* Дата создания ПТ в формате ДД.ММ.ГГГГ*/
				"created_by": "15",
				"created_by$": "Сидоров В.С.", /*Автор ПТ*/
				"created_by$footer_text": "исп: ведущий менеджер УДВ ДКР РБ Иванов И.И. <br />\r\nсот тел: 8 777 777 77 77 \r\n", /*Подпись кем создан*/
				"created_by$login": "vasil",/*Автор Логин*/
				"cur_id": "1",
				"cur_id$": "KZT",/*Валюта ПТ*/
				"extacc_code": "KZ000000000000000000",/*Счет клиента*/
				"extacc_id": "6460",
				"extacc_id$": "Наименование счета клиента",/*Наименование Счета клиента*/
				"id": "18183",
				"knp_id": "290",
				"knp_id$code": "423", /*Код назначения платежа*/
				"knp_id$": "423.Погашение долгосрочных займов (более одного года)",
				"loan_debt": "86429.87",/*Сумма долга по кредиту*/
				"loan_doc_at_fmt": "01.01.2020",
				"loan_id": "20562",
				"loan_id$dbz_num": "RBEZ20-700/XX-000XXX", /*Номер ДБЗ*/
				"loan_id$title": "ФИО Клиента", /*ФИО Клиента ДБЗ*/
				"paid_amount": "111.00", /* Оплаченная сумма */
				"purpose": "Погашение задолженности по ПТ ФИО Клиента по Договору банковского займа № RBEZ20-700/XX-000XXX от 01.01.2020, ИИН 000000000000 в соответствии со ст.32 Закона РК № 11-VI от 26.07.2016 г.  \"О платежах и платежных системах\"", /*Назначение платежа*/
				"reg_id": "454", /*Номер реестра*/
				"reg_id$": "454",
				"stat_id": "2008",
				"stat_id$": "Сформирован на бумажном носителе", /*Статус*/
				"sys$uuid": "b9faab90-75a9-4f6b-ad05-eb9b72bc8d37",
				"transitacc_id": "5",
				"transitacc_id$": "KZ009980000000000000", /*Номер транзитного счета*/
				"updated_at": "2021-10-20T18:23:14.244243+06:00",
				"updated_by": "15",
				"updated_by$": "ФИО Кем изменен",/*ФИО Кем изменен*/
				"updated_by$footer_text": "исп: ведущий менеджер УДВ ДКР РБ Иванов И.И. <br />\r\nсот тел: 8 777 777 77 77 \r\n",/*Подпись кем изменен*/
				"updated_by$login": "vasil" /*логин кем изменен*/
			},
			{
			},
			{
			}
		]
	}


«error_code»:0 - успешный ответ


Сервис приема статусов входящего платежного требования
_______________________________________________________________

POST https://{$k2host}/restapi/services/run/k2req_status_from_eko

.. code-block:: json

     {
          "reference": "PTP00000000001",
          "status_code": "PC1"
     }


.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - reference
     - Референс платежного требования
   * - status_code
     - Статус подтверждения

.. list-table:: Описание статуса
   :header-rows: 1

   * - Описание статуса
     - код статуса
   * - Принята банком
     - PC1
   * - Принята в картотеку банка
     - PC3
   * - Требование исполнено
     - EXECUTED

Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }


«error_code»:0 - успешный ответ


Сервис приема возврата входящего платежного требования
_______________________________________________________________

Запрос:

POST https://{$k2host}/restapi/services/run/k2req_return_from_eko


.. code-block:: json

     {
          "reference": "PTP00000000001",
          "reason_code": "01"
     }

reason_code - причина возврата. смотрите с разделе Настройки К2 -> Причины возврата ПТ.

Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }


«error_code»:0 - успешный ответ



Сервис для получения информации о сканах документов по референсу входящего RZAP
______________________________________________________________________________________________________________________________


.. _k2inforeq_rzap_by_refer:


.. list-table:: Описание запроса:
   :header-rows: 1

   * - Поле
     - Описание
   * - refer
     - Референс RZAP


«error_code»:0 - успешный ответ

.. list-table:: Описание ответа в массиве items:
   :header-rows: 1

   * - Поле
     - Описание
   * - dbz_dt
     - Дата ДБЗ в формате YYYY-MM-DD HH24:MI:SS
   * - dbz_num
     - Номер ДБЗ
   * - file_id
     - ID файла. Поле может отсуствовать, если файл не поступал
   * - iin
     - ИИН клиента
   * - url
     - URL файла


Пример 1. В RZAP всего 1 договор.

.. code-block:: text

	POST http://{$k2host}/restapi/services/run/k2inforeq_rzap_by_refer

.. code-block:: json

	{
		"refer":"HSBKRX0000000001"
	}

Ответ:

.. code-block:: json

	{
		"error_code": 0,
		"error_text": "",
		"items": [
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000000",
				"file_id": "8892",
				"iin": "000000000000",
				"url": "http://127.0.0.1/restapi/getfile?code=CUST-820989b2-b545-496a-be37-5c70a7e9ec79&attachment=true"
			}
		]
	}

Пример 2. В RZAP 3 договора.

.. code-block:: text

	POST http://{$k2host}/restapi/services/run/k2inforeq_rzap_by_refer

.. code-block:: json

	{
		"refer":"HSBKRX0000000002"
	}
	

Ответ:

.. code-block:: json

	{
		"error_code": 0,
		"error_text": "",
		"items": [
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000000",
				"file_id": "8892",
				"iin": "000000000001",
				"url": "http://127.0.0.1/restapi/getfile?code=CUST-820989b2-b545-496a-be37-5c70a7e9ec79&attachment=true"
			},
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000001",
				"file_id": "8894",
				"iin": "000000000002",
				"url": "http://127.0.0.1/restapi/getfile?code=CUST-e72c013d-2a8d-42fd-b267-9917a70fd27f&attachment=true"
			},
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000003",
				"file_id": "8895",
				"iin": "000000000003",
				"url": "http://127.0.0.1/restapi/getfile?code=CUST-030358d4-8028-4475-a5e9-4138dc9f1f7c&attachment=true"
			}
		]
	}


Пример 3. В RZAP 3 договора, но файл поступил только по одному договору.

.. code-block:: text

	POST http://{$k2host}/restapi/services/run/k2inforeq_rzap_by_refer

.. code-block:: json

	{
		"refer":"HSBKRX0000000003"
	}
	

Ответ:

.. code-block:: json

	{
		"error_code": 0,
		"error_text": "",
		"items": [
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000005",
				"file_id": "8896",
				"iin": "000000000005",
				"url": "http://127.0.0.1/restapi/getfile?code=CUST-7f1a0aea-d9b3-472d-a204-7de31e0fd9db&attachment=true"
			},
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000006",
				"iin": "000000000006"
			},
			{
				"dbz_dt": "2020-02-21 00:00:00",
				"dbz_num": "0000000007",
				"iin": "000000000007"
			}
		]
	}




Сервисы , которые вызываем в АБС
------------------------------------------------------

Получить информацию по клиенту
_______________________________________________________________


GET https://{$abs_get_cli_url}?iinbin=000000000000

.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - iinbin
     - ИИН или БИН клиента

Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0,
          "iinbin": "000000000000",
          "fullname": "850210301899",
          "sectecon": 9,
          "residfl": 1
     }

«error_code»:0 - успешный ответ

Список счетов по клиенту
_______________________________________________________________


GET https://{$abs_get_acc_url}?iinbin=000000000000

.. list-table:: Статусы
   :header-rows: 1

   * - Поле
     - Описание
   * - iinbin
     - ИИН или БИН клиента

Ответ:

.. code-block:: json

     {
          "error_text":"",
          "error_code":0,
          "ibans":
          [
               {
                    "iban":"KZ000000000000000000",
                    "accountName":"Наименование счета, обычно ФИО",
                    "ps": "2204191",
                    "system": "way4",
                    "cur": "KZT"
               }
          ]

     }

«error_code»:0 - успешный ответ

.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - iban
     - Номер счета
   * - accountName
     - Наименование счета, обычно ФИО
   * - ps
     - План счетов по ГК
   * - system
     - КОД АБС
   * - cur
     - Валюта

Получить выписку по счету на Дату
_______________________________________________________________

Достаточно вернуть 1 строку выписки по предоставлению кредита:

GET https://{$abs_get_acc_stmt_dt_url}?dep_id=555&id=666&dea_dep_id=777&dea_id=888&dea_code=999&iban=KZ000000000000000000&dt=2020-01-01

.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - dep_id/id/dea_id/dea_dep_id/dea_code
     - DEP_ID/ID/DEA_ID/DEA_DEA_ID/DEA_CODE договора. Предается только для АБС колвир
   * - iban
     - Передается только для договоров Way4
   * - dt
     - Дата в формате ГГГГ.ММ.ДД

Ответ:

.. code-block:: json

     {
          "error_text": "",
          "error_code": 0,
          "stmt": [
               {
                    "purpose": "Предоставление кредита по договору",
                    "amount": 900000,
                    "cur": "KZT",
                    "DC": "D",
                    "out_bal": 900000
               }
          ]
     }


.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - purpose
     - Назначение платежа
   * - amount
     - Сумма
   * - cur
     - Код валюты
   * - DC
     - D -дебет, C - кредит
   * - out_bal
     - Исходящий остаток

«error_code»:0 - успешный ответ

.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - iban
     - Номер счета
   * - accountName
     - Наименование счета, обычно ФИО
   * - ps
     - План счетов по ГК
   * - system
     - КОД АБС
   * - cur
     - Валюта

Получить Скан ДБЗ
_______________________________________________________________


GET https://{$abs_get_pdf_url}?dbz_num=KD0000000&dbz_dt=2020-01-01&iinbin=000000000000&dea_dt=2020-01-01


.. list-table:: Описание полей
   :header-rows: 1

   * - Поле
     - Описание
   * - dbz_num
     - Номер ДБЗ
   * - dbz_dt
     - Дата ДБЗ в формате ГГГГ.ММ.ДД
   * - iinbin
     - ИИН или БИН клиента
   * - dea_dt
     - дата оформления линии

Успешный Ответ:

.. code-block:: text

     Status 200
     Content-Type: application/pdf
     Content-Disposition: attachment; filename="Имяфайла.pdf"
     RAW данные в формате PDF,TIFF


Неуспешный Ответ:

.. code-block:: text

     Status 404

Регистрация ПТ в информационной системе банка
_______________________________________________________________

POST https://{$abs_reg_pt_url}

.. code-block:: json

     {
          "refer": "PTP0000000000001",
          "accept_dt": "2021-01-05",
          "doc_num": "16",
          "doc_at": "2021-01-04",
          "iinbin": "ИИН/БИН клиента",
          "acc_fullname": "Тестовый тест тестович",
          "ben_fullname": "АО \"KASPI BANK\"",
          "ben_bin": "971240001315",
          "ben_iban": "KZ12722R00000000000",
          "ben_kbe": "14",
          "amount": 2000000,
          "cur": "KZT",
          "knp": "423",
          "dbz_num": "R0000-001",
          "dbz_dt": "2014-02-08",
          "purpose": "Безакцептное погашение задолженности заемщика (Тестовый тест тестович) по Договору банковского займа №R0000-001 от 08.02.2014г. ,  в соответствии со ст. 32 Закона РК №11-VI от 26.07.2016г. \"О платежах и платежных системах\".",
          "head":"Руководителев Руководитель Руководителулы",
          "account":"Главный Бухгалер Петрович"
     }

.. list-table:: Описание полей
     :header-rows: 1

     * - Поле
       - Описание
     * - refer
       - Уникальный Референс ПТ
     * - accept_dt
       - Дата приема ПТ в формате ГГГГ.ММ.ДД
     * - doc_num
       - Номер документа
     * - accept_dt
       - Дата ПТ в формате ГГГГ.ММ.ДД
     * - iinbin
       - ИИН или БИН клиента
     * - acc_fullname
       - Наименование счета
     * - ben_fullname
       - Получатель
     * - ben_bin
       - БИН получателя
     * - ben_iban
       - Номер счета получателя
     * - ben_kbe
       - КБе
     * - amount
       - Сумма ПТ
     * - cur
       - Код валюты
     * - knp
       - Код назначения платежа
     * - dbz_num
       - Номер ДБЗ
     * - dbz_dt
       - Дата ДБЗ в формате ГГГГ.ММ.ДД
     * - purpose
       - Назначение платежа
     * - head
       - Руководитель
     * - account
       - Бухгалтер

Ответ

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }


Отзыв ПТ в информационной системе банка
_______________________________________________________________

POST https://{$abs_refuse_pt_url}

.. code-block:: json

     {
          "refer": "PTP0000000000001",
          "reason_code": "01"
     }


reason_code - причина отзыва. смотрите с разделе Документы -> Причины отзывов.



Ответ

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }


Возврат ПТ в информационной системе банка
_______________________________________________________________


POST https://{$abs_return_pt_url}

.. code-block:: json

     {
          "refer": "PTP0000000000001",
          "reason_code": "99"
     }


reason_code - причина возврата. смотрите с разделе Документы -> Причины отзывов.



Ответ

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }


Получение актуальной задолженности по кредиту из Colvir
_______________________________________________________________


POST https://{$colvir_get_loan_debt}

.. code-block:: json

     {
          "dep_id": 2,
          "id": 1001
     }

dep_id/id - Primary Key договора (L_DEA)

Ответ

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
		  "debt":100000
     }


Получение актуальной задолженности по кредиту из Way4
_______________________________________________________________


POST https://{$way4_get_loan_debt}

.. code-block:: json

     {
          "contract_number": "KZ000000000000000000"
     }

contract_number - Уникальный номер контракта.


Ответ

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
		  "debt":100000
     }


Получение списка платежных требований из АБС по фильтру
_______________________________________________________________


POST https://{$get_all_pt_from_abs}

.. code-block:: json

     {
          "page ": 1,
		  "perpage":"2",
		  "ben_bin":"000000000000",
		  "doc_at1":"2021-05-01",
		  "doc_at2":"2021-05-01",
		  "iinbin":"111111111111"
     }

.. list-table:: Описание полей
     :header-rows: 1

     * - Поле
       - Описание
     * - page
       - Номер страницы от 1
     * - perpage
       - Строк на странице, например, 25 страниц. В oracle " OFFSET ? ROWS FETCH NEXT ? ROWS ONLY", в Postgres "limit ? offset ?"
     * - ben_bin
       - Необязательный Фильтр БИН корреспондента
     * - doc_at1
       - Необязательный Фильтр дата документа с
     * - doc_at2
       - Необязательный Фильтр дата документа по
     * - iinbin
       - Необязательный Фильтр по ИИН клиента


Ответ

.. code-block:: json

	[
		"all_count":1000,
		{
			 "refer": "PTP0000000000001",
			 "accept_dt": "2021-01-05",
			 "doc_num": "16",
			 "doc_at": "2021-01-04",
			 "iinbin": "ИИН/БИН клиента",
			 "acc_fullname": "Тестовый тест тестович",
			 "ben_fullname": "АО \"KASPI BANK\"",
			 "ben_bin": "971240001315",
			 "ben_iban": "KZ12722R00000000000",
			 "ben_kbe": "14",
			 "amount": 2000000,
			 "cur": "KZT",
			 "knp": "423",
			 "dbz_num": "R0000-001",
			 "dbz_dt": "2014-02-08",
			 "purpose": "Безакцептное погашение задолженности заемщика (Тестовый тест тестович) по Договору банковского займа №R0000-001 от 08.02.2014г. ,  в соответствии со ст. 32 Закона РК №11-VI от 26.07.2016г. \"О платежах и платежных системах\".",
			 "head":"Руководителев Руководитель Руководителулы",
			 "account":"Главный Бухгалер Петрович"
		},
		{
		},
		{
		}

	]


.. list-table:: Описание полей
     :header-rows: 1

     * - Поле
       - Описание
     * - refer
       - Уникальный Референс ПТ
     * - accept_dt
       - Дата приема ПТ в формате ГГГГ.ММ.ДД
     * - doc_num
       - Номер документа
     * - accept_dt
       - Дата ПТ в формате ГГГГ.ММ.ДД
     * - iinbin
       - ИИН или БИН клиента
     * - acc_fullname
       - Наименование счета
     * - ben_fullname
       - Получатель
     * - ben_bin
       - БИН получателя
     * - ben_iban
       - Номер счета получателя
     * - ben_kbe
       - КБе
     * - amount
       - Сумма ПТ
     * - cur
       - Код валюты
     * - knp
       - Код назначения платежа
     * - dbz_num
       - Номер ДБЗ
     * - dbz_dt
       - Дата ДБЗ в формате ГГГГ.ММ.ДД
     * - purpose
       - Назначение платежа
     * - head
       - Руководитель
     * - account
       - Бухгалтер
     * - all_count
       - Количество записей без фильтра. Для отражения постраничного вывода.


Выгрузка списка исключений из К2 в ЕКО
_______________________________________________________________

Отправка происходит полным списком без частичной загрузки.

Отправка в ЕКО:

POST https://{$post_all_loan_exclude_to_eko}

.. code-block:: json

	{
	  "items": [
	   {
		"bank": "KINCKZKA",
		"finish_dt": "2021-10-16",
		"for_bank": "1",
		"for_extreq": "0",
		"for_iban": "0",
		"for_refuse": "0",
		"id": "19",
		"iin": "981217450830",
		"is_active": "1"
	   },
	   {
		"finish_dt": "2021-10-08",
		"for_bank": "1",
		"for_extreq": "1",
		"for_iban": "1",
		"for_refuse": "1",
		"id": "20",
		"iin": "000000000000",
		"is_active": "0"
	   },
	   {
		"for_bank": "0",
		"for_extreq": "0",
		"for_iban": "0",
		"for_refuse": "0",
		"id": "11",
		"iin": "780204403060",
		"is_active": "0"
	   },
	   {
		"finish_dt": "2021-10-30",
		"for_bank": "0",
		"for_extreq": "0",
		"for_iban": "1",
		"for_refuse": "0",
		"iban": "KZ123456789012345678",
		"id": "9",
		"iin": "780204403060",
		"is_active": "0"
	   },
	   {
		"finish_dt": "2021-10-08",
		"for_bank": "0",
		"for_extreq": "0",
		"for_iban": "0",
		"for_refuse": "0",
		"id": "18",
		"iin": "990615400064",
		"is_active": "0"
	   }
	  ]
	 }

.. list-table:: Описание полей
     :header-rows: 1

     * - Поле
       - Описание
     * - finish_dt
       - Действие запрета в формате YYYY-MM-DD
     * - for_bank
       - Запрет действует для банка в поле bank, если for_bank = "1"
     * - for_extreq
       - Запрет выставления исходящих ПТ
     * - for_iban
       - Запрет действует счета в поле iban, если for_iban = "1"
     * - for_refuse
       - Запрет отзывов ПТ
     * - iban
       - IBAN исключаемого счета
     * - bank
       - БИК исключаемого банка
     * - id
       - Уникальный номер запрета
     * - iin
       - ИИН клиента, по которому производится запрет
     * - is_active
       - Запрет активен, если is_active = "1"


Успешный ответ от ЕКО

.. code-block:: json

     {
          "error_text":"",
          "error_code":0
     }
