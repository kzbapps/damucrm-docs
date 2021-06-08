SendMail2 - Отправить на E-mail
==========================================================================

.. code-block:: lua 


   json = {}
   json.title = v.title
   
   
    
    
    files = array({})
    files["2"] = var.filename
    
    to = array({})
    
    to["1"] = var.email
	

    errText,errNum = SendMail2 (
        
    	--1 --String From
    	GetUserParamValue(sys.user_id,"crm_smtp_user"),
    	--2 --Array To
    	to,
    	--3 --Subject 
    	"Коммерческое предложение",
    	--4 -- Content-Type
    	"text/html",
    	--5 -- Body
    	"Коммерческое предложение",
    	--6 -- Array Files
    	files,
    	--7 -- SMTP Host string
    	GetParamValue("crm_smtp_host"),--"smtp.yandex.ru",
    	--8 -- SMTP Port integer
    	tonumber(GetParamValue("crm_smtp_port")),--587,
    	--9 -- login
    	GetUserParamValue(sys.user_id,"crm_smtp_user"),
    	--10 --password
    	GetUserParamValue(sys.user_id,"crm_smtp_password"),
    	--11 async true/false
    	false
    	
    )         

