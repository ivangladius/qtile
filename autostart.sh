#!/bin/sh

sudo auto-cpufreq --live &
nitrogen --restore &
nm-applet &
#./$HOME/.config/polybar/launch.sh
