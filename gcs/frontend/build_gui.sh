#!/bin/bash
# Build gui from QT Designer ui files
# CUSF 2018

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")"  ; pwd -P )
cd "$parent_path"

#Example syntax:
#pyuic5 ui/main_window.ui -o main_window.py


#general channel widget
pyuic5 ui/Ui_channel_widget.ui -o Ui_channel_widget.py

#5 individual channels
pyuic5 ui/Ui_channel_1.ui -o Ui_channel_1.py
pyuic5 ui/Ui_channel_2.ui -o Ui_channel_2.py
pyuic5 ui/Ui_channel_3.ui -o Ui_channel_3.py
pyuic5 ui/Ui_channel_4.ui -o Ui_channel_4.py
pyuic5 ui/Ui_channel_5.ui -o Ui_channel_5.py

#widget for each block of 5 channels
pyuic5 ui/Ui_AB_widget.ui -o Ui_AB_widget.py

pyuic5 ui/Ui_A_widget.ui -o Ui_A_widget.py
pyuic5 ui/Ui_B_widget.ui -o Ui_B_widget.py


#main window
pyuic5 ui/main_window_real.ui -o main_window_real.py
