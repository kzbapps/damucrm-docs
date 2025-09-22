CryptoSignPKCS1v15 - вычисляет подпись хеширования с использованием RSASSA-PKCS1-V1_5-SIGN из RSA PKCS # 1 v1.5.
================================================================================================================================================================

CryptoSignPKCS1v15 вычисляет подпись хеширования с использованием RSASSA-PKCS1-V1_5-SIGN из RSA PKCS # 1 v1.5. Обратите внимание, что хеширование должно быть результатом хеширования входного сообщения с использованием данной хеш-функции. Если хеш равен нулю, хеш подписывается напрямую. Это не рекомендуется, за исключением возможности взаимодействия.

Если rand не равно нулю, то RSA-ослепление будет использоваться, чтобы избежать атак по побочным каналам по времени.

Эта функция детерминирована. Таким образом, если набор возможных сообщений невелик, злоумышленник может построить карту от сообщений до подписей и идентифицировать подписанные сообщения. Как всегда, подписи обеспечивают подлинность, а не конфиденциальность.

Пример

.. code-block:: lua 

	fullText=[[<contractStatementsRequest>
	<date-begin>2019-02-08T00:00:00+06:00</date-begin><date-end>2019-02-08T23:59:59+06:00</date-end>
	<account-iban>KZ5660XXXXXXXXXX1806</account-iban>
	<contract-id>11111</contract-id>
	</contractStatementsRequest>]]

	pk,errText1,errNum1 = ReadFile("c:/Users/damu/testonlinebank.p12")
	data,cert,errText,errNum = CryptoSignPKCS1v15(pk,"1234",fullText)

	body = "<certificate>" .. Base64Encode(cert).."</certificate>\r\n"..
	"<xmlBody>" .. Base64Encode(fullText).."</xmlBody>\r\n"..
	"<signature>" .. Base64Encode(data).."</signature>\r\n"
			
			
	data = array( { ["Content-type"] = "text/xml;charset=UTF-8" } )

	--output={}
	res = httpPost2("https://services.onlinebank.kz:443/ContractStatementsWebService",data ,

			
	[[<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="http://contractstatements.webservices.onlinebank.kz/">
	   <soapenv:Header/>
	   <soapenv:Body>
		  <con:getStatementsList>
	]]..body..[[
		</con:getStatementsList>
	   </soapenv:Body>
	</soapenv:Envelope>        
	]]

	)


Результат

.. code-block:: xml 

	<certificate></certificate><xmlBody>PGNvbnRyYWN0U3RhXXXXXXXXXXXXXXX8L2RhdGUtYmVnaW4+PGRhdGUtZW5kPjIwMTktMDItMDhUMjM6NTk6NTkrMDY6MDA8L2RhdGUtZW5kPgo8YWNjb3VudXXXXXXXXXXXXXXXXXX50LWliYW4+Cjxjb250cmFjdC1pZD44NTc5NjM8L2NvbnRyYWN0LWlXXXXXXXXXXX1JlcXVlc3Q+</xmlBody><signature></signature>