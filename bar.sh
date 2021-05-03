#!/bin/bash

while true; do
  BAR_STR=$(/home/madaspe/dwm_python_bar/venv/bin/python3 /home/madaspe/dwm_python_bar/bar.py)
  xsetroot -name "$BAR_STR"
  sleep 1
done
