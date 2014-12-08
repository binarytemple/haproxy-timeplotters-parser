haproxy-timeplotters-parser
===========================

Python scripts for converting haproxy log files into a format usable by [timeplotters](http://jkff.info/software/timeplotters ).


Example of script output
```

2014-08-14 00:22:22 =ha_cnt_nosrv.99.82.23.6 1
2014-08-14 00:22:26 =ha_cnt_nosrv.99.82.23.121 1
2014-08-14 00:22:30 =ha_cnt_nosrv.99.82.23.7 1
2014-08-14 00:22:31 =ha_cnt_GET.foostorea01 1
2014-08-14 00:22:31.020000 >ha_chat_99.82_20_12.foostorea01
2014-08-14 00:22:31 <ha_chat_99.82_20_12.foostorea01
2014-08-14 00:22:31 =ha_cnt_size.foostorea01 404
2014-08-14 00:22:31.020000 =ha_cnt_life.foostorea01 -0.02
2014-08-14 00:22:31.020000 =ha_cnt_queue_time.foostorea01 0
2014-08-14 00:22:31.020000 =ha_cnt_connect_time.foostorea01 0
2014-08-14 00:22:31 =ha_cnt_connection.foostorea01 1
2014-08-14 00:22:31.020000 =ha_cnt_total_time.foostorea01 0
2014-08-14 00:22:44 =ha_cnt_PUT.foostorea03 1
2014-08-14 00:22:44.737000 >ha_chat_99.82_20_11.foostorea03
2014-08-14 00:22:44 <ha_chat_99.82_20_11.foostorea03

```
