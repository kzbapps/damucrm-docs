Импорт и обработка Excel файла
=========================================


.. code-block:: lua

	local pkg = dbrequire("pkg/csv")

	local data,errText,errNum = pkg.excel2csv(var.file_id)
	if errNum~=0 then
		var.last_error = errText
		return
	end    

	local rqFields=array({"N квартиры","Имя владельца Телефон"})

	local maps ={}

	for k,v in pairs (data[1]) do
	maps[v]=k
	end


	for k,v in pairs(rqFields) do
		if maps[v]==nil then
			var.last_error="Поле ".. v .."не задано"
			return
		end    
	end    


	for k,v in pairs (data) do

	if k>1 and v[maps["N квартиры"]] =="34"  then
		var.last_error = "Успешно найдена квартира "..v[maps["N квартиры"]].." на строке "..(k-1)
		return
	end    

	end
