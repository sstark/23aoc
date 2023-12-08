#!/bin/zsh

e="AAA"
integer c=0
declare -A m
declare -A lr
set -A lr L 1 R 2

read directions
read
while read line
do
    set $(tr -d '(=,)' <<<$line)
    m[$1]="$2 $3"
done

while [[ $e != "ZZZ" ]]
do
    set $=m[$e]
    e=${(P)${lr[${directions[(c%$#directions)+1]}]}}
    c+=1
done

echo $c
