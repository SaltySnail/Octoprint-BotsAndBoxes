# coding=utf-8
from __future__ import absolute_import, unicode_literals
from jinja2 import Template

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class BotsAndBoxesPlugin(octoprint.plugin.StartupPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.SimpleApiPlugin,
    octoprint.plugin.AssetPlugin
):

    def __init__(self):
       self.commandss=0
       
    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_vars(self):
        return dict(url=self._settings.get(["url"]))

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/BotsAndBoxes.js"],
            css=["css/BotsAndBoxes.css"],
            less=["less/BotsAndBoxes.less"]
        )

    def myfunction(self):
        self._logger.info("Boem Biem BamBoem Biem BamBoem Biem BamBoem Biem BamBoem Biem BamBoem Biem BamBoem Biem BamBoem Biem BamBoem Biem BamBoem Biem Bam")

    def get_api_commands(self):
        self._logger.info("Manually triggered get_api")
        return dict(turnOn=["ip"])

    def on_api_command(self, command, data):
        if command == 'turnOn':
            self._logger.info("Manually triggered!")
    ##~~ AssetPlugin mixin

    #def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
    #    return {
    #        "js": ["js/BotsAndBoxes.js"],
    #        "css": ["css/BotsAndBoxes.css"],
    #        "less": ["less/BotsAndBoxes.less"]
    #    }

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return {
            "BotsAndBoxes": {
                "displayName": "BotsAndBoxes",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "SaltySnail",
                "repo": "OctoPrint-Botsandboxes",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/SaltySnail/OctoPrint-Botsandboxes/archive/{target_version}.zip",
            }
        }


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "BotsAndBoxes"


# Set the Python version your plugin is compatible with below. Recommended is Python 3 only for all new plugins.
# OctoPrint 1.4.0 - 1.7.x run under both Python 3 and the end-of-life Python 2.
# OctoPrint 1.8.0 onwards only supports Python 3.
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = BotsAndBoxesPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
