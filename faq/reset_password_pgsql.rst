Восстановление пароля, имея доступ к базе данных PostgreSQL
================================================================

1. Установим расширение pgcrypto;

.. code-block:: sql

    CREATE EXTENSION pgcrypto

2. Изменим пароль пользователю с id=1 (админу)

.. code-block:: sql
    
    update users set password =  (select  crypt('1234567890',  gen_salt('bf')) ) where id= 1;

