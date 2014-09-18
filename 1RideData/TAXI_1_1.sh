#! /bin/bash
#################################################################################
#     File Name           :     TAXI_1_1.sh
#     Created By          :     xd
#     Creation Date       :     [2014-08-15 19:41]
#     Last Modified       :     [2014-09-06 21:11]
#     Description         :     add one more step to clean the data
#################################################################################

# 38 min processing 33G and writes 21G data
# ouch ... missed 5 days of data ... vim mis-operation
# so 57 min processing 33G and output 30G

foo () {
    # clear empty line
    rm /run/shm/tmp1;
    for i in fullByDay/VehicleData20100901.csv fullByDay/VehicleData20100902.csv fullByDay/VehicleData20100903.csv fullByDay/VehicleData20100904.csv fullByDay/VehicleData20100905.csv fullByDay/VehicleData20100906.csv fullByDay/VehicleData20100907.csv fullByDay/VehicleData20100908.csv fullByDay/VehicleData20100909.csv fullByDay/VehicleData20100910.csv fullByDay/VehicleData20100911.csv fullByDay/VehicleData20100912.csv fullByDay/VehicleData20100913.csv fullByDay/VehicleData20100914.csv fullByDay/VehicleData20100915.csv;
    do
        sed  '/^$/d' $i/$1 >> /run/shm/tmp1
    done 

    # clear first field, and prepare for sort
    # though awk is faster, cut is more clear
    cut -d ',' -f2- /run/shm/tmp1 > /run/shm/tmp2

    # because the raw data are not fully in order
    sort /run/shm/tmp2 > fullByCars/$1
}

for i in $(cat carlist.txt);
do
    echo $i;
    foo $i;
done

