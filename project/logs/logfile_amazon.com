--2020-01-19 16:33:00--  http://amazon.com/
Resolving amazon.com (amazon.com)... 205.251.242.103, 176.32.98.166, 176.32.103.205
Connecting to amazon.com (amazon.com)|205.251.242.103|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:33:01--  https://amazon.com/
Connecting to amazon.com (amazon.com)|205.251.242.103|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:33:01--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 23.43.17.196
Connecting to www.amazon.com (www.amazon.com)|23.43.17.196|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/dev/null’

     0K .......... .......... .......... .......... .......... 73.5M
    50K .......... .......... .......... .......... ..........  101M
   100K .......... .......... .......... .......... .......... 6.15M
   150K .......... .......... .......... .......... .......... 5.39M
   200K .......... .......... .......... .......... .......... 22.8M
   250K .......... .......... .......... .......... ..........  137M
   300K .......... .......... .......... .......... .......... 7.01M
   350K .......... .......... .......... .......... ........    221M=0.2s

2020-01-19 16:33:01 (14.0 Mb/s) - ‘/dev/null’ saved [407653]

--2020-01-19 16:33:01--  http://amazon.com/
Resolving amazon.com (amazon.com)... 176.32.98.166, 176.32.103.205, 205.251.242.103
Connecting to amazon.com (amazon.com)|176.32.98.166|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:33:02--  https://amazon.com/
Connecting to amazon.com (amazon.com)|176.32.98.166|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:33:02--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 23.43.17.196
Connecting to www.amazon.com (www.amazon.com)|23.43.17.196|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/dev/null’

     0K .......... .......... .......... .......... .......... 5.09M
    50K .......... .......... .......... .......... .......... 54.9M
   100K .......... .......... .......... .......... ..........  124M
   150K .......... .......... .......... .......... .......... 11.8M
   200K .......... .......... .......... .......... .......... 4.30M
   250K .......... .......... .......... .......... ..........  158M
   300K .......... .......... .......... .......... ..........  297M
   350K .......... .......... .......... .......... ........   20.4M=0.2s

2020-01-19 16:33:02 (13.3 Mb/s) - ‘/dev/null’ saved [407658]

--2020-01-19 16:35:09--  http://amazon.com/
Resolving amazon.com (amazon.com)... 176.32.98.166, 205.251.242.103, 176.32.103.205
Connecting to amazon.com (amazon.com)|176.32.98.166|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:35:09--  https://amazon.com/
Connecting to amazon.com (amazon.com)|176.32.98.166|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:35:09--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 99.86.254.138
Connecting to www.amazon.com (www.amazon.com)|99.86.254.138|:443... connected.
HTTP request sent, awaiting response... 503 Service Unavailable
2020-01-19 16:35:09 ERROR 503: Service Unavailable.

--2020-01-19 16:41:45--  http://amazon.com/
Resolving amazon.com (amazon.com)... 205.251.242.103, 176.32.103.205, 176.32.98.166
Connecting to amazon.com (amazon.com)|205.251.242.103|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:41:46--  https://amazon.com/
Connecting to amazon.com (amazon.com)|205.251.242.103|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:41:46--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 13.35.240.13
Connecting to www.amazon.com (www.amazon.com)|13.35.240.13|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/dev/null’

     0K .......... .......... .......... .......... .......... 2.71M
    50K .......... .......... .......... .......... .......... 5.49M
   100K .......... .......... .......... .......... ..........  138M
   150K .......... .......... .......... .......... .......... 5.74M
   200K .......... .......... .......... .......... ..........  178M
   250K .......... .......... .......... .......... .......... 5.66M
   300K .......... .......... .......... .......... .......... 64.3M
   350K .......... .......... .......... .......... ........   5.49M=0.5s

2020-01-19 16:41:47 (7.20 Mb/s) - ‘/dev/null’ saved [407984]

--2020-01-19 16:41:47--  http://amazon.com/
Resolving amazon.com (amazon.com)... 176.32.103.205, 176.32.98.166, 205.251.242.103
Connecting to amazon.com (amazon.com)|176.32.103.205|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:41:47--  https://amazon.com/
Connecting to amazon.com (amazon.com)|176.32.103.205|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:41:47--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 13.35.240.13
Connecting to www.amazon.com (www.amazon.com)|13.35.240.13|:443... connected.
HTTP request sent, awaiting response... 503 Service Unavailable
2020-01-19 16:41:47 ERROR 503: Service Unavailable.

--2020-01-19 16:51:14--  http://amazon.com/
Resolving amazon.com (amazon.com)... 176.32.98.166, 176.32.103.205, 205.251.242.103
Connecting to amazon.com (amazon.com)|176.32.98.166|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:51:14--  https://amazon.com/
Connecting to amazon.com (amazon.com)|176.32.98.166|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:51:15--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 143.204.191.85
Connecting to www.amazon.com (www.amazon.com)|143.204.191.85|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/dev/null’

     0K .......... .......... .......... .......... .......... 2.69M
    50K .......... .......... .......... .......... .......... 5.62M
   100K .......... .......... .......... .......... ..........  126M
   150K .......... .......... .......... .......... .......... 5.91M
   200K .......... .......... .......... .......... .......... 84.1M
   250K .......... .......... .......... .......... ..........  408M
   300K .......... .......... .......... .......... .......... 5.97M
   350K .......... .......... .......... .......... ........    154M=0.4s

2020-01-19 16:51:15 (8.70 Mb/s) - ‘/dev/null’ saved [407586]

--2020-01-19 16:51:15--  http://amazon.com/
Resolving amazon.com (amazon.com)... 176.32.103.205, 205.251.242.103, 176.32.98.166
Connecting to amazon.com (amazon.com)|176.32.103.205|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:51:15--  https://amazon.com/
Connecting to amazon.com (amazon.com)|176.32.103.205|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:51:16--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 143.204.191.85
Connecting to www.amazon.com (www.amazon.com)|143.204.191.85|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/dev/null’

     0K .......... .......... .......... .......... .......... 1.32M
    50K .......... .......... .......... .......... .......... 1.38M
   100K .......... .......... .......... .......... .......... 1.80M
   150K .......... .......... .......... .......... .......... 2.74M
   200K .......... .......... .......... .......... .......... 1.82M
   250K .......... .......... .......... .......... .......... 2.13M
   300K .......... .......... .......... .......... .......... 2.72M
   350K .......... .......... .......... .......... ..         3.21M=1.7s

2020-01-19 16:51:18 (1.94 Mb/s) - ‘/dev/null’ saved [401957]

--2020-01-19 16:51:18--  http://amazon.com/
Resolving amazon.com (amazon.com)... 205.251.242.103, 176.32.98.166, 176.32.103.205
Connecting to amazon.com (amazon.com)|205.251.242.103|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:51:18--  https://amazon.com/
Connecting to amazon.com (amazon.com)|205.251.242.103|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:51:18--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 143.204.191.85
Connecting to www.amazon.com (www.amazon.com)|143.204.191.85|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘/dev/null’

     0K .......... .......... .......... .......... .......... 2.68M
    50K .......... .......... .......... .......... ..........  638K
   100K .......... .......... .......... .......... .......... 99.9M
   150K .......... .......... .......... .......... ..........  100M
   200K .......... .......... .......... .......... ..........  137M
   250K .......... .......... .......... .......... .......... 5.96M
   300K .......... .......... .......... .......... ..........  175M
   350K .......... .......... .......... .......... .......     304M=0.9s

2020-01-19 16:51:19 (3.71 Mb/s) - ‘/dev/null’ saved [406829]

--2020-01-19 16:51:19--  http://amazon.com/
Resolving amazon.com (amazon.com)... 176.32.98.166, 176.32.103.205, 205.251.242.103
Connecting to amazon.com (amazon.com)|176.32.98.166|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://amazon.com/ [following]
--2020-01-19 16:51:19--  https://amazon.com/
Connecting to amazon.com (amazon.com)|176.32.98.166|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://www.amazon.com/ [following]
--2020-01-19 16:51:20--  https://www.amazon.com/
Resolving www.amazon.com (www.amazon.com)... 143.204.191.85
Connecting to www.amazon.com (www.amazon.com)|143.204.191.85|:443... connected.
HTTP request sent, awaiting response... 503 Service Unavailable
2020-01-19 16:51:20 ERROR 503: Service Unavailable.

