--2020-01-19 16:35:34--  http://whatsapp.com/
Resolving whatsapp.com (whatsapp.com)... 169.55.60.170, 108.168.255.227, 169.55.60.148, ...
Connecting to whatsapp.com (whatsapp.com)|169.55.60.170|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://www.whatsapp.com/ [following]
--2020-01-19 16:35:34--  https://www.whatsapp.com/
Resolving www.whatsapp.com (www.whatsapp.com)... 157.240.1.53
Connecting to www.whatsapp.com (www.whatsapp.com)|157.240.1.53|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://www.whatsapp.com/unsupportedbrowser [following]
--2020-01-19 16:35:34--  https://www.whatsapp.com/unsupportedbrowser
Reusing existing connection to www.whatsapp.com:443.
HTTP request sent, awaiting response... 404 Not Found
2020-01-19 16:35:34 ERROR 404: Not Found.

--2020-01-19 16:56:27--  http://whatsapp.com/
Resolving whatsapp.com (whatsapp.com)... 169.55.60.148, 108.168.254.65, 108.168.255.227, ...
Connecting to whatsapp.com (whatsapp.com)|169.55.60.148|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://www.whatsapp.com/ [following]
--2020-01-19 16:56:27--  https://www.whatsapp.com/
Resolving www.whatsapp.com (www.whatsapp.com)... 157.240.1.53
Connecting to www.whatsapp.com (www.whatsapp.com)|157.240.1.53|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://www.whatsapp.com/unsupportedbrowser [following]
--2020-01-19 16:56:27--  https://www.whatsapp.com/unsupportedbrowser
Reusing existing connection to www.whatsapp.com:443.
HTTP request sent, awaiting response... 404 Not Found
2020-01-19 16:56:27 ERROR 404: Not Found.

