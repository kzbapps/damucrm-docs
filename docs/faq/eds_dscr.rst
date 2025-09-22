Описание работы ЭЦП в DamuBPM
==================================================================================================

Формирование ЭЦП на JavaScript
----------------------------------------

Если в маршруте документа указан вид задачи «Подписание», то документ должен пройти процедуру подписание посредством наложения электронной цифровой подписи.

 
.. image:: img/eds_dscr/image001.jpg
  :width: 100%
  :alt: Alternative text
  
  
При назначении задачи «Подписание» у подписанта появляется соответствующая кнопка:
 
.. image:: img/eds_dscr/image002.jpg
  :width: 100%
  :alt: Alternative text
  

При нажатии на «Подписать с ЭЦП» открывается диалоговое окно:
Необходимо

1.	Выбрать файл GOST – Закрытый ключ в формате .p12 для наложения ЭЦП файл 

2.	Ввести пароль от закрытого ключа

При наложении ЭЦП:

1.	закрытый ключ не отправляется на сервер:

Как видим, нет сетевой активности:

.. image:: img/eds_dscr/image003.jpg
  :width: 100%
  :alt: Alternative text

2.	подписание происходит через браузерные библиотеки web-crypto алгоритмом GOST 34.311-95 with GOST 34.310-2004(1.2.398.3.10.1.1.1.2)
3.	Подписывается вложенный файл в формате Base64



.. image:: img/eds_dscr/image004.png
  :width: 100%
  :alt: Alternative text



Валидация ЭЦП на сервере
----------------------------------------

2.1.	Отправляется открытая ЭЦП на сервер, а также подписываемый файл:

.. image:: img/eds_dscr/image005.jpg
  :width: 100%
  :alt: Alternative text

В ответ получаем ок:

.. image:: img/eds_dscr/image006.jpg
  :width: 100%
  :alt: Alternative text

2.2. Пункты Валидации.
1.	Проверка на отзыв сертификата
2.	Проверка срока действия сертификата
3.	Проверка принадлежности по БИН организации
4.	Проверка целостности методом Kalkan VerifyData
5.	Проверка корневых сертификатов
6.	Проверка на алгоритм GOST 34.311-95 with GOST 34.310-2004(1.2.398.3.10.1.1.1.2)


Наложение Временной метки (Timestamp / TSP)
------------------------------------------------------

При нажатии на кнопку Дальше продолжается процесс согласно схеме BPMN:

.. image:: img/eds_dscr/image007.jpg
  :width: 100%
  :alt: Alternative text

Происходит дополнительная валидация ЭЦП на сервере (см 2.2. Пункты Валидации).

Наложение Метки времени (TimeStamp / TSP через http://tsp.pki.gov.kz) на сервере и наложение OCSP через (http://ocsp.pki.gov.kz)

Сохранение ЭЦП в таблицу files_eds

Наложение QR-кода, добавление страницы
-------------------------------------------------

После того, как подписант наложил ЭЦП, в документе возле файла появится значок «Ключ»

.. image:: img/eds_dscr/image008.jpg
  :width: 100%
  :alt: Alternative text
  
 

При нажатии на файл откроется файл в формате PDF с наложенными QR кодами:

.. image:: img/eds_dscr/image009.jpg
  :width: 100%
  :alt: Alternative text 
  

Информацией об ЭЦП в подвале каждой странице:

.. image:: img/eds_dscr/image010.jpg
  :width: 100%
  :alt: Alternative text 

и дополнительной страницей с информацией об ЭЦП:


.. image:: img/eds_dscr/image011.jpg
  :width: 100%
  :alt: Alternative text

Проверка ЭЦП через сервис ezsigner.kz
-----------------------------------------------

Для проверки юридической значимости ЭЦП во внешнем сервисе ezsigner.kz, разработанным АО «Национальные информационные технологии», под администратором зайдем в Настройки->Файлы:

.. image:: img/eds_dscr/image012.jpg
  :width: 100%
  :alt: Alternative text

Найдем файл по имени, убедимся, что есть галочка Наличие ЭЦП:

.. image:: img/eds_dscr/image013.jpg
  :width: 100%
  :alt: Alternative text

Щелкним на строку с файлом и перейдем к детализации Файла:

В открывшемся файле детализация нажмем перейти в табличной части «Электроннные цифровые подписи»

.. image:: img/eds_dscr/image014.jpg
  :width: 100%
  :alt: Alternative text

Нажмем на «ЭЦП для ezsigner.kz»

.. image:: img/eds_dscr/image015.jpg
  :width: 100%
  :alt: Alternative text

Скачается файл:

.. image:: img/eds_dscr/image016.png
  :width: 100%
  :alt: Alternative text

Переходим на сайт ezsigner.kz, нажимаем Проверить документ:


.. image:: img/eds_dscr/image017.jpg
  :width: 100%
  :alt: Alternative text

Нажимаем Choose File /Выбрать файл

.. image:: img/eds_dscr/image018.jpg
  :width: 100%
  :alt: Alternative text

Выбираем файл:

.. image:: img/eds_dscr/image019.jpg
  :width: 100%
  :alt: Alternative text

Нажимаем проверить:

.. image:: img/eds_dscr/image020.jpg
  :width: 100%
  :alt: Alternative text

На экране видим информацию об электронном документе. Все проверки ЭЦП прошли успешно:

.. image:: img/eds_dscr/image021.jpg
  :width: 100%
  :alt: Alternative text


Для извлечения оригинала документа нажмите Извлечь документ:

Скачается файл в формате Base64.


.. image:: img/eds_dscr/image022.png
  :width: 100%
  :alt: Alternative text

Откройте блокнотом скаченный файл, скопируйте содержимое текста в буфер обмена.

.. image:: img/eds_dscr/image023.jpg
  :width: 100%
  :alt: Alternative text


В браузере введите следующую строку:

data:application/octet-stream;base64,СОДЕРЖИМОЕ ИЗ БУФЕРА ОБМЕНА

.. image:: img/eds_dscr/image024.jpg
  :width: 100%
  :alt: Alternative text
  
И нажмите Enter

Скачается файл, переименуйте расширение файла в .docx.

.. image:: img/eds_dscr/image025.png
  :width: 100%
  :alt: Alternative text

Открываем и видим оригинал документа:

.. image:: img/eds_dscr/image026.jpg
  :width: 100%
  :alt: Alternative text