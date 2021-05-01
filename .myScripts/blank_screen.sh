#!/bin/bash

timeout="$((60 * 1000 * 120))"
#timeout="$((6 * 1))"
if [ $(xprintidle) -gt $timeout ]
then
    #i3lock;
    xset dpms force off
fi


