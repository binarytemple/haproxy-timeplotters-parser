#!/usr/bin/env python 

import sys
from dateutil import parser

file=sys.argv[1:]

if not file:
    print "please specify input file as argument to this script"
    exit(1)

count = 0
with open(file[0], 'r') as f:
    for line in f:
        try:
            fields = line.split()
            start=parser.parse("%s %s %s" % (fields[0],fields[1],fields[2]))
            if fields[8].find("UP") > -1:
                dhost=fields[6].split("/")[1]
                print "%s !ha_host_up.%s " % (start,dhost) 
                continue

            if fields[8].find("DOWN") > -1:
                dhost=fields[6].split("/")[1]
                print "%s !ha_host_down.%s " % (start,dhost) 
                continue

            end=parser.parse(fields[6][1:-1].replace("/","-").replace(":"," ",1))
            
            measure=fields[10]
            dhost=fields[8].split("/")[1]
            shost=fields[5].split(":")[0]
            sport=fields[5].split(":")[1]
            
            queue_time=fields[9].split("/")[0]
            connect_time=fields[9].split("/")[1]
            total_time=fields[9].split("/")[2]
            
            if dhost == "<NOSRV>":
                print "%s =ha_cnt_nosrv.%s 1" % (start,shost)
                continue
            
            if len(fields) > 16:
                method=fields[17].replace('"','')
                if method == "PUT" or method == "GET" or method == "DELETE":
                    print "%s =ha_cnt_%s.%s 1"  % (start,method,dhost)

            req_thread="ha_chat_%s.%s" % ( shost.replace(".","_"),dhost.replace(".","_") ) 

            print "%s >%s" % (end,req_thread)
            print "%s <%s" % (start,req_thread  )
   
            print "%s =ha_cnt_size.%s %s"  % (start,dhost,measure)
            print "%s =ha_cnt_life.%s %s" %  (end,dhost,(start - end).total_seconds()) 
            print "%s =ha_cnt_queue_time.%s %s"  % (end,dhost,queue_time)
            print "%s =ha_cnt_connect_time.%s %s"  % (end,dhost,connect_time)
            print "%s =ha_cnt_connection.%s 1"  % (start,dhost)
            print "%s =ha_cnt_total_time.%s %s"  % (end,dhost,total_time)
            
        except Exception,e:
            sys.stderr.write("%s - %s - %s"  % (e, line, sys.exc_info()[0]  ))
            continue
