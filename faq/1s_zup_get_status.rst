Интеграция с 1С - ЗУП: обновить статусы сотрудников
==================================================================================================

.. code-block:: lua

	output={}

	sqlPositions=[[select zup.status_code, zup.CostCenter, zup.NameDivis, zup.NameDolj, zup.TabNum, zup.FIO, zup.IIN,  zup.StatusStartDate id
	from (select master.sys.fn_varbintohexstr(StatusD._Fld18879RRef ) status_code , Divis._Description CostCenter,Divis._Fld30174 NameDivis,Dolj._Description NameDolj, Fiz._Code TabNum,Fiz._Description FIO,
				 Fiz._Fld6379 IIN,Fiz._IDRRef ID_Fiz,Divis._IDRRef ID_Divis, Dolj._IDRRef ID_Dolj,
				 ROW_NUMBER () OVER (PARTITION BY StatusF._Fld19518RRef ORDER BY MAX(StatusD._Fld18880) DESC) AS StatusStartDate,
				 ROW_NUMBER () OVER (PARTITION BY Fiz._Description ORDER BY MAX(StatusF._Period) DESC) AS num
		  from   _InfoRg19517 StatusF, _Reference260 Fiz, _Reference157 Divis,_Reference68 Dolj, _InfoRg18875 StatusD

		  where StatusF._Fld19520RRef = Fiz._IDRRef and
				StatusF._Fld19522RRef = Divis._IDRRef and
				StatusF._Fld19526RRef = Dolj._IDRRef and
				StatusF._Fld19518RRef = StatusD._Fld18876RRef and
				Fiz._Fld6379 not in ( select _Fld6379 from _Reference260 where _IDRRef in (select _Fld19520RRef from _InfoRg19517 where _Fld19523RRef = 0xB33DFC9B1619F433433E45BE20908286))
		  group by Divis._Description, Divis._Fld30174, Dolj._Description, Fiz._Code, Fiz._Description, Fiz._Fld6379, Fiz._IDRRef, Divis._IDRRef,Dolj._IDRRef, StatusD._Fld18880,StatusD._Fld18879RRef,StatusF._Fld19518RRef

	)zup

	where num=1 
	]]
	arrPositions,output.error_text,output.error_code = SqlQueryRowsExtDb("ZUP_Work83",
		
		sqlPositions


	)

	output.arrPositions =array(arrPositions)
	  if output.error_code~=0 then
		  return
	  end 
	  
	 
	for k,v in pairs (arrPositions) do
		output.error_text,output.error_code = SqlExec2([[update users set stat_id = (select id from user_stat where code= ?) where login = ?]],v.status_code, v.TabNum)
		SqlExec2("commit")
		  if output.error_code~=0 then
			  return
		  end     
	  
	end

