Отправить файл на другой сервер через lua
=========================================


.. code-block:: lua


	local arr,errText,errNum=SqlQueryRows([[select file_id from its_d_esedo_in_file where its_d_esedo_in_id=?]],var.id)

	if errNum~=0 then
		var.last_error = errText
		return
	end


	http = require("pkg/http")

	local boundary = UUID()
	for k,v in pairs(arr) do
		local filename,contentType,raw,errText,errNum = FileContent(v.file_id,sys.user_id)
		if errNum~=0 then
			var.last_error = errText
			return
		end    
		
		local headers = array(
		{
		[ "Content-Type" ]  = "multipart/form-data; boundary="..boundary ,
		}
		)    
		
	local data = "--"..boundary.."\r\n"..
	"Content-Disposition: form-data; name=\"file\"; filename=\"".. filename.. "\"\r\n"..
	"Content-Type: image/jpeg\r\n"..
	"\r\n"..
	raw..
	"\r\n"..
	"--"..boundary.."\r\n"

		
	local resData, errText,errNum = http.post ("https://external.server.com/restapi/upload?dir=CUST",data, headers)

	if errNum~=0 then
		var.last_error = errText
		return
	end    



		
	end