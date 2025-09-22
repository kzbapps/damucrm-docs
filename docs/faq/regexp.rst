LUA Регулярные выражения
=========================


Пример работы с регулярными выражениями

.. code-block:: lua

	local regexp=require("goluago/regexp")  

	function regexpMatch(s,rx)
	local re = regexp.compile(rx) 
	return re.findSubmatch(s or '')  
	end
	  
	local r=regexpMatch(line, [[^/([^/]+)/(.+)$]])
	if #r>0 then
		key=field..'_'..r[2]
		mt[key]=r[3]
	else 
		mt[key]=(mt[key] or '') .. line
	end
	
Пример проверки пароля

.. code-block:: lua

	local regexp=require("goluago/regexp")  
	local re = regexp.compile("[^A-Za-z!@#$%^&*]") 
	found = re.findAllSubmatch("!ПриветABC",-1)
