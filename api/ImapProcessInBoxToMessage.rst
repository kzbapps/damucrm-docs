Imap process in box to message - oбработка получения входящей электронной почты
======================================================================================================================

.. code-block:: lua

     the_last_uid ,

     error_text ,
 
     error_code = ImapProcessInBoxToMessage ( 
  
                                             input.channel.smtp_user,
 
                                             input.channel.smtp_password ,

                                             input.channel.imap_host..":"..input.channel.imap_port , 

                                             input.channel_imap_script ,
 
                                             tonumber(1) , 
       
                                             tonumber(input.channel.imap_last_uid+1) ,
 
                                             tonumber (input.channel/manager_id)
 
                                            )
