Настройка и проверка работы ЭЦП
==================================================================================================

Распаковать папку  в /opt/kalkancrypt

в env прописать

LD_LIBRARY_PATH=:/opt/kalkancrypt/:/opt/kalkancrypt/lib/engines

Centos/RHEL/Oracle Linux:

.. code-block:: bash

	yum install pcsc-lite
	
Debian/Ubuntu:

.. code-block:: bash

	apt install libpcsclite-dev	

.. code-block:: bash

	systemctl restart damu

Пример проверки ЭЦП
	
.. code-block:: lua

	output={}

	crypto=require("pkg/crypto")
	--xml=[[<data><in:R01 xmlns:in="http://aisoip.adilet.gov.kz/webservices/BANK/types/Request"><in:items><in:BankID>99999</in:BankID></in:items></in:R01></data>]]

	output.ersurl,output.ernurl=crypto.TSASetUrl("http://tsp.pki.gov.kz:80")
	--output.signedxml,output.erssign,output.ernsign=crypto.SignXml(xml,'/data/*')

	xml=request.input.signxml

	cert,output.ers1,output.ern1=crypto.GetCertFromXml(xml)
	cert=StrReplace(cert," ","",-1)

	regexp=require('goluago/regexp')
	function regexpMatch(s,rx,n)
		local re = regexp.compile(rx) 
		return re.findSubmatch(s or '')[n] 
	  end

	ser,output.ers2,output.ern2=crypto.CertificateGetInfo(cert,0x0000080d)
	output.iin=regexpMatch(ser,'IIN(\\d{12})',2)
	output.cn,output.ers2,output.ern2=crypto.CertificateGetInfo(cert,0x0000080a)
	output.fio=regexpMatch(output.cn,'CN=(.+)\\0',2)
	notBefore,output.ers2,output.ern2=crypto.CertificateGetInfo(cert,0x00000813)
	output.notBefore1=regexpMatch(notBefore,'notBefore=(.+)\\0',2)
	notAfter,output.ers2,output.ern2=crypto.CertificateGetInfo(cert,0x00000814)
	output.notAfter1=regexpMatch(notAfter,'notAfter=(.+)\\0',2)
	output.notBefore2 = TimeParseFormat(output.notBefore1,"02.01.2006 15:04:05 MST","2006-01-02 15:04:05")
	output.notAfter2 = TimeParseFormat(output.notAfter1,"02.01.2006 15:04:05 MST","2006-01-02 15:04:05")
	output.ers1,output.ern1=crypto.LoadCertificateFromFile('/opt/certs/test/t/root_rsa.cer',0x00000201)
	output.ers2,output.ern2=crypto.LoadCertificateFromFile('/opt/certs/test/t/nca_rsa.cer',0x00000202)
	output.ersv,output.ernv=crypto.VerifyXml(xml or '')
	
