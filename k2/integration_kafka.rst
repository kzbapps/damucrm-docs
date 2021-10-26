Описание интеграции через Kafka
==================================================================================================

Данный раздел описывает интеграции с системой Картотека обременений(К2) через Kafka

Отправка в Kafka
---------------------------

Сервис отправки статуса в Loxon через Kafka
_______________________________________________________________

Запрос

.. code-block:: json

		{
			"event_date": "2006-01-02 15:04:05",
			"bik": "HSBKKZKX",
			"referer": "PTP0000000000001",
			"contract_number": "KD0000000001",
			"debt": 8000.01,
			"amount": 10000.01,
			"status": "request was sent"

		}


.. list-table:: Описание полей
     :header-rows: 1

     * - Поле
       - Описание
     * - event_date
       - Дата события в формате YYYY-MM-DD HH24:MI:SS
     * - bik
       - БИК Банка
     * - referer
       - Референс Платежного требования
     * - contract_number
       - Номер ДБЗ
     * - debt
       - Долг по кредиту на момент события
     * - amount
       - Сумма платежного требования




.. list-table:: Значение статусов
     :header-rows: 1

     * - Статус
       - Описание на русском
     * - request was sent
       - запрос отправлен
     * - request confirmed
       - запрос подтвержден
     * - payment order activated
       - ПТ активировано
     * - payment order executed
       - ПТ исполнено
     * - payment order was reversed
       - ПТ возвращено
     * - payment order de activated
       - ПТ отозвано


