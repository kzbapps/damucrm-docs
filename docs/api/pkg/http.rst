
Работа с HTTP-запросами через pkg/http в DamuBPM (Lua)
=======================================================

Модуль ``pkg/http`` предназначен для выполнения HTTP-запросов (GET, POST, PUT, DELETE) в сценариях на Lua. 
Он используется для интеграции с внешними сервисами и API, обеспечивая гибкую настройку заголовков, тела запроса и параметров соединения.

.. contents:: Содержание
   :local:
   :depth: 2

Обзор и сигнатуры
-----------------

Модуль ``pkg/http`` выполняет HTTP-запросы с поддержкой SSL, позволяет передавать заголовки, тело, таймаут и по запросу возвращать заголовки ответа.

.. code-block:: lua

   -- Основные функции:
   http.get(url, headers, timeout, returnHeaders)
   http.post(url, body, headers, timeout, returnHeaders)
   http.put(url, body, headers, timeout, returnHeaders)
   http.delete(url, headers, timeout, returnHeaders)

Возвращаемые значения
---------------------

Каждая функция возвращает кортеж из трёх значений:

.. code-block:: lua

   local response, errorMessage, statusCode = http.<method>( ... )

- ``response`` — тело ответа сервера (string, может содержать JSON/текст).
- ``errorMessage`` — текст ошибки (если запрос завершился с ошибкой).
- ``statusCode`` — код статуса. ``0`` при успехе, иначе содержит код ошибки или статус.

Параметры функций
-----------------

- ``url`` — строка с адресом ресурса (например, ``https://example.com/api``).
- ``body`` — строка с данными запроса (обычно JSON) для POST/PUT.
- ``headers`` — таблица Lua с заголовками (например, ``{ ["Content-Type"]="application/json" }``).
- ``timeout`` — число секунд ожидания ответа.
- ``returnHeaders`` — логический флаг; если ``true``, модуль вернёт заголовки ответа вместе с телом.

Примеры использования
---------------------

http.post — отправка данных
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: lua

   local http = require("pkg/http")

   local url = "https://example.com/api/create"
   local body = "{"name":"John"}"
   local headers = {
      ["Content-Type"] = "application/json"
   }
   local timeout = 60
   local returnHeaders = false

   local response, errorMessage, statusCode = http.post(url, body, headers, timeout, returnHeaders)

   if statusCode == 0 then
      print("Ответ: " .. response)
   else
      print("Ошибка: " .. errorMessage .. ", код статуса: " .. statusCode)
   end

http.get — получение данных
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: lua

   local http = require("pkg/http")

   local url = "https://example.com/api/data"
   local headers = {
      ["Authorization"] = "Bearer token"
   }
   local timeout = 60
   local returnHeaders = true

   local response, errorMessage, statusCode = http.get(url, headers, timeout, returnHeaders)

   if statusCode == 0 then
      print("Ответ: " .. response)
   else
      print("Ошибка: " .. errorMessage .. ", код статуса: " .. statusCode)
   end

http.put — обновление ресурса
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: lua

   local http = require("pkg/http")

   local url = "https://example.com/api/resource"
   local body = "{"key":"value"}"
   local headers = {
      ["Content-Type"] = "application/json"
   }
   local timeout = 30
   local returnHeaders = true

   local response, errorMessage, statusCode = http.put(url, body, headers, timeout, returnHeaders)

   if statusCode == 0 then
      print("Ответ: " .. response)
   else
      print("Ошибка: " .. errorMessage .. ", код статуса: " .. statusCode)
   end

http.delete — удаление ресурса
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: lua

   local http = require("pkg/http")

   local url = "https://example.com/api/resource/123"
   local headers = {
      ["Authorization"] = "Bearer token"
   }
   local timeout = 45
   local returnHeaders = false

   local response, errorMessage, statusCode = http.delete(url, headers, timeout, returnHeaders)

   if statusCode == 0 then
      print("Ресурс удалён: " .. response)
   else
      print("Ошибка: " .. errorMessage .. ", код статуса: " .. statusCode)
   end

Рекомендации и лучшие практики
------------------------------

- Всегда указывайте ``Content-Type`` при передаче JSON или форм.
- Используйте ``timeout`` для защиты от зависания запросов.
- Обрабатывайте ``statusCode`` и ``errorMessage`` для корректной реакции на ошибки.
- Включайте ``returnHeaders``, если нужны метаданные (например, ``Set-Cookie``).
- Для тестирования удобно использовать сервис ``https://httpbin.org``.

Совет: если API возвращает JSON, разберите ``response`` через библиотеку ``cjson``.
