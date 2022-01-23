Пример подписания ЭЦП SmartBridge
==================================================================================================

в env прописать

.. code-block:: text

	LD_LIBRARY_PATH=:/opt/kalkancrypt/:/opt/kalkancrypt/lib/engines




.. code-block:: lua

	local  http=require("pkg/http")

	function setBody(id,s)

	   local a,ers,ern= SqlCall([[update k2_mj_xml_log set body=:s where id=:id]],
			 {
				s = { input=true, output=false,value=s,clob = true },
				id = { input=true, output=false,value=tostring(id)}
			} 
		)
	   if ern ~=0 then error(ern) end
	end

	function makeRequest(serviceId,requestData,instance_id)
		local crypto=require('pkg/crypto')
		local ers,ern=crypto.LoadKey("/opt/k2/bank.pfx","12345678") --todo: to params
		if ern ~=0 then 
			print(ers) 
		end
		local session_id=UUID()
		local requestMessageId,errText,errNum=DML("insert","k2_mj_xml_log",1,{instance_id = instance_id, session_id=session_id , io='O' })
		local messageDate=EntityValueById("k2_mj_xml_log","created_at",requestMessageId)
		messageDate= TimeParseFormat(messageDate,"2006-01-02 15:04:05 -0700 -07","2006-01-02T15:04:05")
		
		local senderId='bank'
		local password='*********'


		local xmlReqIn=[[<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
		<SOAP-ENV:Header xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"/>
		<soap:Body>
			<io:SendMessage xmlns:io="http://bip.bee.kz/SyncChannel/v10/Types">
			<request>
				<requestInfo>
				<messageId>]] .. HTMLEscapeString(requestMessageId)  ..  [[</messageId>
				<serviceId>]] .. HTMLEscapeString(serviceId)  ..  [[</serviceId>
				<messageDate>]] .. HTMLEscapeString(messageDate)  ..  [[</messageDate>
				<sender>
					<senderId>]] .. HTMLEscapeString(senderId) .. [[</senderId>
					<password>]] .. HTMLEscapeString(password) .. [[</password>
				</sender>
				<sessionId>]] .. HTMLEscapeString(session_id) .. [[</sessionId>
				</requestInfo>
				<requestData> ]] .. requestData .. [[</requestData>
			</request>
			</io:SendMessage>
		</soap:Body>
		</soap:Envelope>]]
		
		local xmlReq,ers,ern=crypto.SignXml( xmlReqIn ,"//request/requestData/data/*")
		if ern ~=0 then return '',0,0,ers,ern end
		setBody(requestMessageId,xmlReq)
	   
		local headers = array( { ["Content-type"] = " text/xml;charset=\"utf-8\"" } )
		local mjUrl=GetParamValue("k2mj_url")
		local row1=nil
		local res=nil
		row1,ers,ern=SqlQueryRow2('select * from(select id,body,nord from k2_mj_xml_log_mockup t where t.sta=1 order by nord) t where rownum=1')
		if ern==0 then
			 res=row1.body
			local xx,ers,ern= SqlCall([[update k2_mj_xml_log_mockup set sta=2 where id=:id ]],
				 {
					id = { input=true, output=false,value=tostring(row1.id)}
				} 
			)
		else
			 res,ers,ern=http.post(mjUrl,xmlReq,headers)
			if ern ~=0 then return '',0,0,ers,ern end
		end
	   -- print("end k2_mj_xml_log_mockup")
		
		local responseMessageId,errText,errNum=DML("insert","k2_mj_xml_log",1,{ instance_id = instance_id, session_id=session_id , io='I'})
		
		--print("end k2_mj_xml_log_mockup777",responseMessageId)
		 setBody(responseMessageId,res)
		 
		--print("end k2_mj_xml_log_mockup888") 
		return res,requestMessageId,responseMessageId,'',0
	end

	return makeRequest

