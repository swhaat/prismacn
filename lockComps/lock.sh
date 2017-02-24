#! /bin/bash

## to block computers
#disable mouse REPLACE "X" with mouse device number
#disable keyboard REPLACE "Y" with keyboard device number
block_comps () {
ssh usuario@$HOST bash -c "xscreensaver-command -activate &&
						  xinput set-int-prop 3 'Device Enabled' 8 0 &&
						  xinput set-int-prop 2 'Device Enabled' 8 0"
}

enable_comps () {
ssh usuario@$HOST bash -c "xscreensaver-command -deactivate &&
						  xinput set-int-prop 3 'Device Enabled' 8 1 &&
						  xinput set-int-prop 2 'Device Enabled' 8 1"
}

## to block computers
#xscreensaver-command -activate
##disable mouse REPLACE "X" with mouse device number
#xinput set-int-prop X "Device Enabled" 8 0
##disable keyboard REPLACE "Y" with keyboard device number
#xinput set-int-prop Y "Device Enabled" 8 0


##to activate computers
#xscreensaver-command -deactivate
##enable mouse 
#xinput set-int-prop X "Device Enabled" 8 1
##enable keyboard
#xinput set-int-prop Y "Device Enabled" 8 1

##notification
#notify-send 'Hello world!' 'This is an example notification.' --icon=dialog-information
