Поддержка DAV для онлайн редактирования файлов через текстовые редакторы (MSWord,MSExcel и другие)
==================================================================================================

DamuCRM поддерживает технологию DAV для онлайн редактирования файлов через текстовые редакторы (MSWord,MSExcel и другие)

1. Укажите галочку DAV в вашей папки. Внимание!!! Данная функция позволит любому пользователю изменять файлы в этой папке без авторизации!!!

2. Загрузите файл (Через веб-интерфейс, через lua (UploadRawData) или через rest api).

3. Получите UUID файла (files.code)

4. Редактируйте файл по ссылке: ms-word:ofe|u|<cloud_url>restapi/dav/<КОД_ПАПКИ>/<КОД_ФАЙЛА>/<ИМЯ_ФАЙЛА>

	например,
	
.. code-block:: html


	<a href="ms-word:ofe|u|https://127.0.0.1/restapi/dav/dav/dav-d999703b-c220-486d-89ff-040d8ad233b1/Привет.docx">Редактировать</a>

При сохранении в (MSWord,MSExcel и другие) файл будет изменяться мгновенно в файловом хранилище или в вашем S3 хранилище
