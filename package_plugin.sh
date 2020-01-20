#!/usr/bin/env bash
export FILE_NAME=plugin.zip
rm -rf $FILE_NAME
cd plugins/bots || exit
zip -r ../../$FILE_NAME *
