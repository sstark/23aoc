#!/bin/zsh

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
while read _ _ data
do
    DATA=${data//(,|;)/}
    power=$(($(max red)*$(max green)*$(max blue)))
    res+=$power
done

print $res
