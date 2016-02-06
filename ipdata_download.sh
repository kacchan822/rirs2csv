#!/bin/bash
#
# Copyright (c) 2016 Katsuya SAITO
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#
# @(#) ipdata_download.sh ver.0.1.0 2016.02.05
#

today=`date +%Y%m%d%H%M%S`

for url in `cat source_url`
do
	name=`echo ${url} | sed -e 's/.*\/delegated-\(.*\)-extended-latest$/\1/g'`
	wget --timeout=30 -O archive/${name}-${today} ${url} 

    if [ -e archive/${name}-${today} ]; then
	        ln -fs archive/${name}-${today} ./${name}
    fi
done

files=`cat source_url | sed -e 's/.*\/delegated-\(.*\)-extended-latest$/\1/g'`
cat ${files} > rirsfiles

exit 0
