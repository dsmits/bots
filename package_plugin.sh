#!/usr/bin/env bash
export FILE_NAME=plugin.zip
rm -rf $FILE_NAME
cd plugin || exit
zip -r ../$FILE_NAME *
