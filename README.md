# ZHA Controlled Hue Dimmer Switch
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs) [![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/) 

<a href="https://www.buymeacoffee.com/so3n" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

Fully customize the buttons on a ZHA controlled Philips Hue Dimmer Switch.
  
## Installing
Install via [HACS](https://hacs.xyz/). Alternatively, place the apps folder and its contents in your appdaemon folder.

## Configuration

### Main Config options

| Variable | Type   | Required                                   | Description                                                                                                                                                                                                                                                              |
| -------- | ------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| module   | string | True                                       | Set to `zha_hue_dimmer_switch`                                                                                                                                                                                                                                           |
| class    | string | True                                       | Set to `HueDimmerSwitch`                                                                                                                                                                                                                                                 |
| switch   | string | True                                       | `IEEE` of the Hue Dimmer Switch. This can be found by going to the integrations page on HA, and under Zigbee Home Automation click on [configure] > [devices] and then click on the device belonging to the Hue Dimmer Switch. `IEEE` will be listed under `Zigbee Info` |
| light    | string | True (unless using advanced configuration) | `entity_id` of the light to control                                                                                                                                                                                                                                      |
| advanced | list   | False                                      | Optional. Customize the actions for each button. See below                                                                                                                                                                                                               |


### **Advanced** Config options

| Variable       | Type   | Required | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `button event` | string | True     | Set the name of the variable to one of the button events you want to customize: `on_press`, `on_hold`, `on_short_release`, `on_long_release`, `up_press`, `up_hold`, `up_short_release`, `up_long_release`, `down_press`, `down_hold`, `down_short_release`, `down_long_release`, `off_press`, `off_hold`, `off_short_release`, `off_long_release` |
| action_type    | string | True     | Service call to execute. Valid options: `turn_on`, `turn_off`, `toggle` or `cycle`                                                                                                                                                                                                                                                                 |
| entity         | string | True     | `entity_id` of the device to control                                                                                                                                                                                                                                                                                                               |
| parameters     | dict   | False    | Optional. Specify the parameters to use for the service call (eg. `brightness`, `rgb_color`, `flash`, etc). Can include a list of parameters for the cycle option                                                                                                                                                                                  |



### Basic Example

```yaml
dimmer_bedroom:
  module: zha_hue_dimmer_switch
  class: HueDimmerSwitch
  switch: '00:00:00:00:00:00:00:00'
  light: light.bedroom
```

This sets up `light.bedroom` to be controlled by the Hue Dimmer Switch using the default button configuration:

* `ON` button turns on the light. Each additional press cycles through 33%, 67% and 100% brightness.
* `INCREASE BRIGHTNESS` button increases the brighness 10%
* `DECREASE BRIGHTNESS` button decreases the brighness 10%
* `OFF` button turns off the light.

### Advanced Example

```yaml
dimmer_main:
  module: zha_hue_dimmer_switch
  class: HueDimmerSwitch
  switch: '00:00:00:00:00:00:00:00'
  advanced:
    on_short_release: 
      action_type: toggle
      entity: light.kitchen
      parameters:
        brightness: 255
        kelvin: 4000
    up_short_release: 
      action_type: toggle
      entity: light.dining
      parameters:
        brightness: 255
        kelvin: 3500
    down_short_release: 
      action_type: toggle
      entity: light.living_room
      parameters:
        color_name: red
    off_short_release: 
      action_type: cycle
      entity: light.floor_lamp
      parameters:
        - brightness_pct: 33
          kelvin: 3000
        - brightness_pct: 67
          kelvin: 3000
        - brightness_pct: 100
          kelvin: 3000
        - brightness_pct: 0
```
This advanced config customizes the buttons on the Hue Dimmer Switch as follows::

* `ON` button toggles kitchen light on/off. When turned on the light is set to full brightness and 4000 kelvin color temp.
* `INCREASE BRIGHTNESS` button toggles dining light on/off. When turned on the light is set to full brightness and 3500 kelvin color temp.
* `DECREASE BRIGHTNESS` button toggles living room light on/off. When turned on, color of light is red.
* `OFF` button cycles through the following settings with each button press: 1) 33% brightness 3000 kelvin; 2) 67% brightness 3000 kelvin; 3) 100% brightness 3000 kelvin; and 4) off.


<hr/>

<a href="https://www.buymeacoffee.com/so3n" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
