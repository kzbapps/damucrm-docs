Как отправить Email
=========================
Простой способ: Необходимо перейти в di_chs, добавить SMTP настройки.
Используя скрипт произвести отправку:


.. code-block:: lua

    LoadScript("email_send_by_ch_id")
    errText,errNum = email_send_by_ch_id(email,subject,body,GetParamValue("email_notify_ch_id"),{},true)
    return "",0


Более сложный способ: Используя SendMail2


.. code-block:: lua

	output= {}

	files = array({})
	files["1"] = "c:\\HaxLogs.txt"
	files["2"] = "c:\\ftconfig.ini"
	files["3"] = "c:\\hwupgradewizard.log"

	to = array({})

	to["1"] = "gates@bill.com"
	to["ZZZ"] = "steve@job.com"

	output.errText,output.errNum = SendMail2 (
		
		--1 --String From
		"damucrm@damucrm.com",
		--2 --Array To
		to,
		--3 --Subject
		"Hello From Lua!",
		--4 -- Content-Type
		"text/html",
		--5 -- Body
		"Hello <b>Bob</b> and <i>Cora</i>!",
		--6 -- Array Files
		files,
		--7 -- SMTP Host string
		"smtp.gmail.com",
		--8 -- SMTP Port integer
		587,
		--9 -- login
		"damucrm@damucrm.com",
		--10 --password
		"mysecretpassword",
		--11 async true/false
		true
		
		)