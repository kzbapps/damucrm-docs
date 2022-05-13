Установка сертификатов pki.gov.kz на юридическое лицо для nginx
===================================================================================

Сконвертировать полученный p12

.. code-block:: bash

	openssl pkcs12 -in RSA256_e05aa0f6640ebb066596837cac46ea9673d91e22.p12 -clcerts -nokeys -out esedo.crt
	openssl pkcs12 -in RSA256_e05aa0f6640ebb066596837cac46ea9673d91e22.p12 -nocerts -nodes -out esedo.key

Добавить в nginx

.. code-block:: text

    listen 443 ssl;
    ssl_certificate /etc/ssl/esedo.crt;
    ssl_certificate_key /etc/ssl/esedo.key;

