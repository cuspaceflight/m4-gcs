#!/bin/bash
# Build gui from QT Designer ui files
# CUSF 2018

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")"  ; pwd -P )
cd "$parent_path"

#Example syntax:
pyuic5 ui/main_window.ui -o main_window.py
