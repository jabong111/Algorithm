#!/bin/bash

SWITCH_NAME="$1"
DIR_NAME="$2"
MAIN_FILE="main.py"

if [ -z ${SWITCH_NAME} ] ; then
	echo "must input file name."
	exit
fi

if [ -z ${DIR_NAME} ] ; then
	echo "must input folder name."
	exit
fi

if [ "${SWITCH_NAME}" = "main" ] ; then
	echo "main.py is not apropriate name"
	exit
fi

if [ -e ${MAIN_FILE} ] ; then
	mv main.py ${SWITCH_NAME}.py;
	mv ${SWITCH_NAME}.py ${DIR_NAME}
	cp .tmp.py main.py;
else
	echo "not exist main.cpp"
	exit
fi

echo "file name : ${SWITCH_NAME}.py , folder name : ${DIR_NAME}"


