#!/bin/bash

# MURPHY'S PING SWEEPER

# Inspiration and walkthrough courtesy of TCM Security: Practical Ethical Hacking <https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course>

if [ "$1" == "" ]
then
echo "Does not compute! Please check your syntax."
echo "./murphy_ping_sweep.sh [Required: Net ID- ##.##.##] [Optional: Min Host ID (Default 1)] [Optional: Max Host ID (Default 254)]"

elif [[ "$1" == "-h" ]]||[[ "$1" == "--help" ]]
then
echo "Proper syntax provided below!"
echo "./murphy_ping_sweep.sh [Required: Net ID- ##.##.##] [Optional: Min Host ID (Default 1)] [Optional: Max Host ID (Default 254)]"

elif [ "$2" == ""]
then
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done

elif [ "$3" == ""]
then
for ip in `seq $2 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done

else
for ip in `seq $2 $3`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi