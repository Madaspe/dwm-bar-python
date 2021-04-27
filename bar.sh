#!/bin/bash

while true; do
  BAR_STR=$(python3 bar.py)
  xsetroot -name "$BAR_STR"
  sleep 1
done
