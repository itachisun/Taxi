#! /bin/bash
#################################################################################
#     File Name           :     TAXI_1_1.sh
#     Created By          :     xd
#     Creation Date       :     [2014-08-15 19:41]
#     Last Modified       :     [2014-08-15 19:54]
#     Description         :     add one more step to clean the data
#################################################################################

echo $1

# clear empty line
sed  '/^$/d' $1 > /run/shm/tmp1

# clear first field, and prepare for sort
# though awk is faster, cut is more clear
cut -d ',' -f2- /run/shm/tmp1 > /run/shm/tmp2

sort /run/shm/tmp2 > $1
