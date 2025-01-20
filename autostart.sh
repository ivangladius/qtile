#!/bin/sh

sudo auto-cpufreq --live &
nitrogen --restore &
nm-applet &
volumeicon &
#./$HOME/.config/polybar/launch.sh
