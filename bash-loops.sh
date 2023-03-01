#!/bin/bash

# What a result does the script return?

a=0
while test $a -lt 5; do
	a=$((a+1))
done
echo $a

b=0
true | while test $b -lt 5; do
	b=$((b+1))
done
echo $b
