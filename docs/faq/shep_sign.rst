Подписание XML для отправки в ШЭП
==================================================================================================

.. code-block:: lua

	output = {}	
	local pkgxml=require("pkg/xml")
	local crypto=require('pkg/crypto')
	ers,ern=crypto.LoadKey("/opt/damu/keys/GOSTKNCA_*****************.p12","**********")
	local request_uuid = UUID()
	local body = [[<soapenv:Body Id="]]..  request_uuid..[[">
			<ns2:SendMessage xmlns:ns2="http://bip.bee.kz/SyncChannel/v10/Types"
							 xmlns:ns3="http://bip.bee.kz/common/v10/Types"
							 xmlns:ns4="http://payments.bee.kz/UsageStatusPayment"
							 xmlns:ns5="http://integration.elicense.kz/eokno/exchangeservice"
							 xmlns:ns6="https://icweb/IICWebService">
				<request>
					<requestInfo>
						<messageId>00000000-9228-4bf4-8880-72280e728e92</messageId>
						<serviceId>GBDFL_UniversalServiceSync</serviceId>
						<messageDate>2022-02-07T15:13:33.159+06:00</messageDate>
						<sender>
							<senderId>*****</senderId>
							<password>*****</password>
						</sender>
					</requestInfo>
					<requestData>
						<data>
							<iin>00000000000</iin>
							<messageId>123456789</messageId>
							<messageDate>2016-12-06T00:00:00.000+06:00</messageDate>
							<senderCode>DAMUBPM</senderCode>
						</data>
					</requestData>
				</request>
			</ns2:SendMessage>
		</soapenv:Body>]]


	local data = [[<?xml version="1.0" encoding="UTF-8"?>
	<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" >
	<soapenv:Header></soapenv:Header>
	]]
	..body..
	[[</soapenv:Envelope>]]

	local dsNS={ds="http://www.w3.org/2000/09/xmldsig#"}
	local soapNS={soapenv="http://schemas.xmlsoap.org/soap/envelope/"}
	local soapheader,container,ers,ern=pkgxml.ExtractXml(data,soapNS,'//soapenv:Header') --remove header
	if ern~=0 then  output = "ERR1"..ers..debug.traceback()  return end 
	local signedData,ers,ern=crypto.SignXml(container,'',request_uuid)
	if ern~=0 then  output = "ERR2"..ers..debug.traceback()  return end 
	local certInfo,ers,ern = crypto.GetCertFromXml(signedData)
	if ern~=0 then  output = "ERR3"..ers..debug.traceback()  return end
	local xmlsign,container,ers,ern=pkgxml.ExtractXml(signedData,dsNS,'//ds:Signature')
	if ern~=0 then  output = "ERR4"..ers..debug.traceback() return end 
	xmlsign,ers,ern=pkgxml.SetAttr(xmlsign,dsNS,'//ds:Signature',"Id",'ptpsign')
	if ern~=0 then  output = "ERR5"..ers..debug.traceback()  return end
	data,ers,ern=pkgxml.InsertXml(data,soapNS,'//soapenv:Header',xmlsign)
	if ern~=0 then  output = "ERR6"..ers..debug.traceback()  return end
	output=data


Подписание тела запроса:

.. code-block:: lua

	output = {}
	local crypto=require('pkg/crypto')
	ers,ern=crypto.LoadKey("/opt/damu/keys/GOSTKNCA_************.p12","*********")
	local xmlReqIn=[[<?xml version="1.0" encoding="UTF-8" standalone="no"?><ns3:requestDataType xmlns:ns3="http://gbdulinfobybin_v2.egp.gbdul.tamur.kz" xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"><BIN>000000000000</BIN><RequestorBIN>00000000000</RequestorBIN></ns3:requestDataType>]]
	output,aa,a=crypto.SignXml( xmlReqIn ,"")