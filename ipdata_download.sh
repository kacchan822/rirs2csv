#/bin/bash

today=`date +%Y%m%d%H%M%S`

for url in `cat source_url`
do

	name=`echo ${url} | sed -e 's/.*\/delegated-\(.*\)-extended-latest$/\1/g'`
	wget --timeout=30 -O archive/${name}-${today} ${url} 

    if [ -e archive/${name}-${today} ]; then
	        ln -fs ../archive/${name}-${today} ./${name}
    fi

done

files=`cat source_url | sed -e 's/.*\/delegated-\(.*\)-extended-latest$/\1/g'`

cat ${files} > rirsfiles

exit 0
