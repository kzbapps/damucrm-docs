Сформировать вложенный JSON на основе двух SQL
==================================================

.. code-block:: lua

	if request.get.cat_id~=nil and  request.get.cat_id~="" then

		output.attrs,errTExt,errNum = SqlQueryRows([[select a.id,a.title from skk_cat c
		join skk_tpl t on t.id=c.tpl_id 
		join skk_tpl_grp g on g.skk_tpl_id  = t.id
		join skk_tpl_attr a on a.skk_tpl_grp_id = g.id 
		where c.id=?]],request.get.cat_id) 
		
		
		
		local  attr_vals ,errTExt,errNum = SqlQueryRows([[select a.id as attr_id, av.id,av.title from skk_cat c
		join skk_tpl t on t.id=c.tpl_id 
		join skk_tpl_grp g on g.skk_tpl_id  = t.id
		join skk_tpl_attr a on a.skk_tpl_grp_id = g.id 
		join skk_tpl_attr_val av on av.skk_tpl_attr_id =a.id
		where c.id=?]],request.get.cat_id) 
		
		for k,v in pairs(output.attrs) do
			if v.values == nil then
				v.values = array({})
			end
			
			for k1,v1 in pairs(attr_vals) do
				if v1.attr_id == v.id then
					table.insert(v.values,{id = v1.id, title = v1.title})
				end    
			end		
		end
	else
		 output.attrs =array({})
	end
	
Пример ответа:
	
.. code-block:: json

	{ "attrs": [
			{
				"id": "6",
				"title": "Цвет",
				"values": [
					{
						"id": "11",
						"title": "белые"
					},
					{
						"id": "12",
						"title": "красные"
					},
					{
						"id": "13",
						"title": "голубые"
					},
					{
						"id": "14",
						"title": "розовые"
					},
					{
						"id": "15",
						"title": "оранжевые"
					}
				]
			}
		]
	}