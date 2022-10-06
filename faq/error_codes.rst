Справочник по кодам ошибок
================================

.. list-table:: Справочник по кодам ошибок
     :header-rows: 1

     * - Код ошибки
       - Описание
       - Рекомендации
     * - E-BPM-00028
       - CreateInstance.SaveVariables error: pq: SAVEPOINT can only be used in transaction blocks
       - Нарушена транзакционность, не используйте Вместо SqlExec2("commit") используйте Commit()
     * - exit status 77
       - Нет доступа к /home/user, возможно libreoffice Не может запуститься
       - mkdir /home/user, chown user:user /home/user -R
