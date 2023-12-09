#!/bin/zsh

declare -A nums=(one 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9)

find_match () {
    local num
    local s=$1
    for num in ${(k)nums}
    do
        if [[ $s =~ "^$num" ]]
        then
            print $nums[$num]
            return
        fi
    done
    for num in ${(v)nums}
    do
        if [[ $s =~ "^$num" ]]
        then
            print $num
            return
        fi
    done
}

while read line
do
    for i in {1..$#line}
    do
        found=$(find_match $line[$i,-1])
        if [[ -n $found ]]
        then
            num1=$found
            break
        fi 
    done
    for i in {1..$#line}
    do
        found=$(find_match $line[-$i,-1])
        if [[ -n $found ]]
        then
            num2=$found
            break
        fi 
    done
    print "$num1$num2"
done
