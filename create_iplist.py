#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Katsuya SAITO
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#
# version: 0.1.0 (2016.02.05)
#

# import modules ---------------------------------------------------------------------------------#
import ipaddress
import csv
#----------------------------------------------------------------------------- import modules ----#

# Config -----------------------------------------------------------------------------------------#
rirsFile = 'rirsfiles'                                   # RIR statistic exchange format file
outFile = 'ipdata.csv'                                   # OUT PUT FILE
#----------------------------------------------------------------------------- Config ------------#

# Script -----------------------------------------------------------------------------------------#

## IP data load ---------------------------------------#
"""
    rirsFile format:
        The version line format:
            version|registry|serial|records|startdate|enddate|UTCoffset
        The summary line format:
            registry|*|type|*|count|summary
        The record line format:
            registry|cc|type|start|value|date|status[|extensions...]
"""

f = open(rirsFile, 'r')
reader = csv.reader(f, delimiter='|', quoting=csv.QUOTE_NONE)
rirsList = []
for row in reader:
    if len(row) >= 7 and row[2] == 'ipv4':
        rirsList.append(row)
f.close
#-------------------------------------------------------#

# Create IP/CIDR --------------------------------------#
"""
    ipCidrList format:
        [registry,country_code,network_addr,cidr,subnetmask,addr_cidr,
            addr_subnetmask,count_of_adresses,status_make_date,status]
"""
ipCidrList = []
for row in rirsList:
    ipstart = ipaddress.IPv4Address(row[3])  #row[3]:rirsFile record line [start]
    addresses = int(row[4])                  #row[4]:rirsFile record line [value]
    iplast = ipstart + (addresses - 1)

    for ipaddr in ipaddress.summarize_address_range(ipstart,iplast):
        ipaddrmask = ipaddr.with_netmask
        ipdata = [row[0],
                    row[1],
                    ipaddrmask.split('/')[0],
                    str(ipaddr).split('/')[1],
                    ipaddrmask.split('/')[1],
                    ipaddr,
                    ipaddrmask,
                    ipaddr.num_addresses,
                    row[5],
                    row[6]]
        ipCidrList.append(ipdata)

#------------------------------------------------------#

## WRITE CSV FILE -------------------------------------#
"""
    outputFile format: field delimiter ',' as CSV file format
        registry,country_code,network_addr,cidr,subnetmask,addr_cidr,
            addr_subnetmask,count_of_adresses,status_make_date,status
"""
f = open(outFile, 'w')
writecsv = csv.writer(f, lineterminator='\n')
writecsv.writerows(ipCidrList)
f.close()
#------------------------------------------------------#
#----------------------------------------------------------------------------- Script ------------#
