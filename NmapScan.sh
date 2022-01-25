#!/bin/bash 

for ip in $(cat IPs.txt); do nmap -T4 -A -p- -vvv $ip &
done