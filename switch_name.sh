#!/bin/bash

SWITCH_NAME="$1"
DIR_NAME="$2"
MAIN_FILE="main.cpp"

if [ -z ${SWITCH_NAME} ] ; then
	echo "must input file name."
	exit
fi

if [ -z ${DIR_NAME} ] ; then
	echo "must input folder name."
	exit
fi

if [ "${SWITCH_NAME}" = "main" ] ; then
	echo "main.cpp is not apropriate name"
	exit
fi

if [ -e ${MAIN_FILE} ] ; then
	mv main.cpp ${SWITCH_NAME}.cpp;
	mv ${SWITCH_NAME}.cpp ${DIR_NAME}
	cp .tmp.cpp main.cpp;
	make clean;
else
	echo "not exist main.cpp"
	exit
fi

echo "file name : ${SWITCH_NAME}.cpp , folder name : ${DIR_NAME}"


