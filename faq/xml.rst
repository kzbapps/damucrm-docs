Работа с XML в lua
=========================
XML to JSON(table)

.. code-block:: lua

    local mxj=require("pkg/mxj")
    local resJson,ers,ern=mxj.XmlToJson(res)    
    if resJson.Envelope.Body.Fault~=nil and  resJson.Envelope.Body.Fault.faultstring~=nil  then
    	 return "", resJson.Envelope.Body.Fault.faultstring,4
    end
