Настройка мультиязычности для справочников
==================================================


1. Создайте 2 атрибута в сущности вашего справочника:

	1.1: title_kk String (250)

	1.2: title_ru String (250)

2. Заполните поля title_kk - на казахском, title_ru - на русском в справочнике

3. В сущности в поле Дополнительно->Выражение для выборки пропишите:

.. code-block:: sql

	case when :lang='kk' then main.title_kk else main.title_ru end title

4. В атрибуте title во вкладке binding 

	4.1: поставьте галочку Is Formula.

	4.2: В поле формула пропишите: 

	.. code-block:: sql
	
		case when :lang='kk' then main.title_kk else main.title_ru end

5. Опубликуйте сущность.

