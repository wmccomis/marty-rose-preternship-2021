#!/bin/bash

name=$(basename $0)
echo $name
for file in *;
    do
        if [ "$file" != "$name" ];
        then
            if [ -x $file ];
            then
                 #time ./$file | grep -E "real*[0-9]m[0-9]\.[0-9]{3}" | cut -d ' ' -f 2
            fi
        fi
    done
exit $1
