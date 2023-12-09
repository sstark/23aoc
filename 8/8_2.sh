#!/bin/zsh

start_elems=(GPA GTA VDA BBA AAA VSA)
integer c=0
declare -A m
declare -A lr
declare -a paths
set -A lr L 1 R 2

read directions
read
while read line
do
    set $(tr -d '(=,)' <<<$line)
    m[$1]="$2 $3"
done

for e in $start_elems
do
    while [[ $e != *Z ]]
    do
        set $=m[$e]
        e=${(P)${lr[${directions[(c%$#directions)+1]}]}}
        c+=1
    done
    paths+=($c)
    c=0
done

python -c "import math; print(math.lcm(${(j:, :)paths}))"

