while read l; do a=$(sed 's/^[^0-9]*\([0-9]\).*/\1/'<<<$l); b=$(sed 's/.*\([0-9]\)[^0-9]*$/\1/'<<<$l); echo $a$b; done <in1 | summate
