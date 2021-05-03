#!/bin/bash

ABSOLUTE_FILEPATH=`readlink -e "$0" | sed "s/\/bar.sh//"`

VENV=`ls $ABSOLUTE_FILEPATH | grep venv`

if [[ $VENV ]]
then
	PYTHON_BIN="$ABSOLUTE_FILEPATH/venv/bin/python3"

else 
	PYTHON_BIN="python3"
fi

BAR_FILE="$ABSOLUTE_FILEPATH/bar.py"

while true; do
  BAR_STR=$($PYTHON_BIN $BAR_FILE)
  xsetroot -name "$BAR_STR"
  sleep 1
done
