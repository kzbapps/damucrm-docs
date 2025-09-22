insert or update on table violates foreign key constraint 
====================================================================================================

Что делать, если вышла ошибка

pq: insert or update on table "ИмяСущности" violates foreign key constraint "<ИМЯ_ВНЕШНЕГО_КЛЮЧА>"

При сохранении?

Значит привязанный ранее справочник создал Внешний ключ, который неверно ссылается на другую таблицу.

Например, если код Внешнего ключа

its_hr_premiya_hr_position_id_hr_position_family_fk

,

то удаляем поле hr_position_id через действие Удалить поле.

Изменим Reference hr_position_family на hr_position

И опубликуем сущность.
