#!/bin/zsh

RED=12
GREEN=13
BLUE=14

# maximum number for color $1
max () {
    local num col max=0
    for num col in $=DATA
    do
        if [[ $col == $1 ]] && [[ $num -gt $max ]]
        then
            max=$num
        fi
    done
    print $max
}

integer res=0
while read _ id data
do
    id=${id%:}
    DATA=${data//(,|;)/}
    if     [[ $(max red) -le $RED ]] \
        && [[ $(max green) -le $GREEN ]] \
        && [[ $(max blue) -le $BLUE ]]
    then
        res+=$id
    fi
done

print $res
