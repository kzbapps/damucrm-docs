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
			"pt_referer": "PTP0000000000001",
			"refuse_referer": "OP10000000000001",
			"req_referer": "EAR0000000000001",
			"contract_number": "KD0000000001",
			"debt": 8000.01,
			"amount": 10000.01,
			"paid_amount": 2000,
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
     * - pt_referer
       - Референс Платежного требования. Опционально
     * - refuse_referer
       - Референс отзыва или возврата. Опционально
     * - req_referer
       - Референс запроса. Опционально
     * - contract_number
       - Номер ДБЗ
     * - debt
       - Долг по кредиту на момент события
     * - amount
       - Сумма платежного требования
     * - paid_amount
       - Оплаченная сумма платежного требования



.. list-table:: Значение статусов
     :header-rows: 1

     * - Status name eng
       - Status name ru
     * - request was sent
       - запрос отправлен
     * - payment order accepted
       - ПТ принято банком
     * - payment order activated
       - ПТ активировано
     * - payment order not accepted
       - ПТ не принято
     * - not reversed (payment order non-exist)
       - Отзыв ПТ не принят, отзываемый документ
     * - reversal of payment order was not accepted (PO already deactivated)
       - Отзыв ПТ не принят, ПТ возвращено либо ПТ исполнено
     * - payment order reversed
       - ПТ отозвано
     * - Payment order executed
       - ПТ исполнено
