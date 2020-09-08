"""
Customise the buttons on a Hue Dimmer Switch integrated with ZHA
https://github.com/nickneos/Appdaemon-ZHA-Hue-Dimmer-Switch
"""
from appdaemon.plugins.hass.hassapi import Hass


class HueDimmerSwitch(Hass):
    """Define a Hue Dimmer Switch base feature"""

    def initialize(self):
        """Initialize AppDaemon App"""

        # get config values
        self.light = self.args.get("light", None)
        self.switch = self.args.get("switch")
        self.button_config = self.args.get("advanced", None)

        # integer counter used for cycle function
        self.cycle_idx = -1

        # check for basic config
        if not self.button_config:
            if not self.light:
                self.log("Light entity needs to be specified", level="ERROR")
                return

            # default button config if advanced config not specified
            self.button_config = {
                "on_short_release": {
                    "action_type": "cycle",
                    "entity": self.light,
                    "parameters": [
                        {"transition": 0, "brightness_pct": 33},
                        {"transition": 0, "brightness_pct": 67},
                        {"transition": 0, "brightness_pct": 100}
                    ]
                },
                "off_short_release": {
                    "action_type": "turn_off",
                    "entity": self.light,
                    "parameters": {"transition": 0}
                },
                "up_short_release": {
                    "action_type": "turn_on",
                    "entity": self.light,
                    "parameters": {"brightness_step_pct": 10, "transition": 0}
                },
                "down_short_release": {
                    "action_type": "turn_on",
                    "entity": self.light,
                    "parameters": {"brightness_step_pct": -10, "transition": 0}
                }
            }

        # listener for dimmer switch press
        self.listen_event(self.button_pressed_cb, "zha_event", device_ieee=self.switch)


    def button_pressed_cb(self, event_name, data, kwargs):
        """Take action when button is pressed on dimmer switch."""

        # get button event
        button_name = data["command"]

        # call action function if button event is defined in button config
        if button_name in self.button_config:
            self.action(self.button_config[button_name])


    def action(self, button_config):
        """Call the respective service based on the passed button config."""

        # get values from button_config
        action_type = button_config["action_type"]
        entity = button_config["entity"]
        parameters = button_config.get("parameters", {})

        # handle cycle action
        if action_type == "cycle":
            parameters = [parameters] if type(parameters) is not list else parameters
            self.cycle_action(entity, parameters)
            return

        # reset index to -1 on turn_off
        if action_type == "turn_off":
            self.cycle_idx = -1

        # lets do this
        self.call_service(
            f"{entity.split('.')[0]}/{action_type}",
            entity_id=entity,
            **parameters
        )


    def cycle_action(self, light, param_list):
        """Cycle through the parameter list with each button press"""


        # when index -1, turn on light with previous settings
        if self.cycle_idx == -1:
            parameters = {}
        # otherwise get paramaters from list using index value
        else:
            try:
                parameters = param_list[self.cycle_idx]
            except IndexError:
                self.cycle_idx = 0
                parameters = param_list[self.cycle_idx]

        # lets do this
        self.call_service(
            f"{light.split('.')[0]}/turn_on",
            entity_id=light,
            **parameters
        )

        # increment index for next button press
        self.cycle_idx += 1
