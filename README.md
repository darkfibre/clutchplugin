## clutchplugin - Joystick Gremlin plugin for clutch paddles
Plugin for Joystick Gremlin to set bite point for F1-style clutch paddles. Designed to work with the Advanced Paddle Module on SRM-converted Fanatec wheels.

### Background ###

If you have a Fanatec wheel with clutch paddles and you use a [Sim Racing Machines USB Conversion](https://www.simracingmachines.com/WebShop/diy), then you probably want to consider this plugin. It re-implements the clutch bite point functionality that was lost when converting the wheel to USB.

### Prerequisites ####

* Install and configure [vJoy](https://github.com/shauleiz/vJoy/releases)
  * You must **REBOOT** after configuration.
* Install [Joystick Gremlin](https://whitemagic.github.io/JoystickGremlin/download/)

### Joystick Gremlin Setup ###

* Run Joystick Gremlin and go to the **Plugins** tab.
* Add a plugin, select the clutchplugin.py file you downloaded from this repository.
* Click on the small gear to configure the plugin.
	* Make sure the correct vJoy device is selected.
	* Assign paddles and key bindings for adjusting bite point
* Click on the **Activate** button on the toolbar. 
* **Save** the configuration in Joystick Gremlin, you can also make it auto-activate in the settings if you prefer.
* *Optional:* Launch **vJoy Monitor** and verify the buttons on the vJoy device are triggered as you press different buttons.

### iRacing Setup ###

* Ensure the controls you assigned in Joystick Gremlin are not *also* assigned in iRacing, as this may give unexpected results.
* Launch iRacing and go to **Options -> Controls**
  * Alt-Tab to Joystick Gremlin and go to **Tools -> Input Repeater**, this will enable a feature to repeat your most recent input multiple times on the virtual device, designed to assist in assigning controls.
  * Alt-Tab back to iRacing, select **second clutch**.
  * Pull and release one of the paddles, wait a few seconds for iRacing to recognize the re-activation of the vjoy axis.
  * Click **Done**.
  * Go back to Joystick gremlin and **disable the Input Repeater**.
* Hop in a car and test it out. Pull the left clutch paddle and use the Increment/Decrement controls to adjust the bite point. Pull the right paddle for full clutch engagement.

Once you find the sweet spot, you can change the **"Default Bite Point"** back in the plugin configuration, so you don't have to configure it every time. Note that any change to the plugin config requires you to **Deactivate / Activate** Joystick Gremlin again.

Please note that the plugin is only working when Joystick Gremlin is running and the config is **Active**. Simply exiting Joystick Gremlin will revert your controls to their original behavior. I suggest enabling the "Use custom controls for this car" feature for the vehicles you intend to use with this plugin.
