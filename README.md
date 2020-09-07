# ZHA Controlled Hue Dimmer Switch
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs) [![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/) 

<a href="https://www.buymeacoffee.com/so3n" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

Customize the buttons on a ZHA controlled Hue Dimmer Switch.

## Features
* TBA
  
## Installing
Install via [HACS](https://hacs.xyz/). Alternatively, place the apps folder and its contents in your appdaemon folder.

## Configuration

### Main Config options

| Variable | Type           | Required | Default | Description                                                                                       |
| -------- | -------------- | -------- | ------- | ------------------------------------------------------------------------------------------------- |
| module   | string         | True     |         | Set to `zha_hue_dimmer_switch`|
| class    | string         | True     |         | Set to `HueDimmerSwitch`|
| switch  | string | True | | `IEEE` of the Hue Dimmer Switch. This can be found by going to the integrations page on HA, and under Zigbee Home Automation click on [configure] > [devices] and then click on the device belonging to the Hue Dimmer Switch. `IEEE` will be listed under `Zigbee Info`|
| light  | string | True (unless using advanced configuration) | | `entity_id` of the light to control |
| advanced | list | False | | Customize the actions for each button. See below |

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

TBA

<hr/>

<a href="https://www.buymeacoffee.com/so3n" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
