# import the library
import screen_brightness_control as sbc
 
# get the monitor names
monitors = sbc.list_monitors()
print(monitors)
 
# now use this to adjust specific screens by name
sbc.set_brightness(25, display=monitors[0])
