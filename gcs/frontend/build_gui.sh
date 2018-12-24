#!/bin/bash
# Build gui from QT Designer ui files
# CUSF 2018

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")"  ; pwd -P )
cd "$parent_path"

#Example syntax:
#pyuic5 ui/main_window.ui -o main_window.py


#widget for each channel
pyuic5 ui/Ui_channel_widget.ui -o Ui_channel_widget.py

#widget for each block of 5 channels
pyuic5 ui/Ui_AB_widget.ui -o Ui_AB_widget.py

#main window
pyuic5 ui/main_window_real.ui -o main_window_real.py
