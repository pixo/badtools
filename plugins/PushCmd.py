'''
Created on Jan 3, 2015

@author: pixo
'''
from badass.plugin import PluginCmd


class PushCmd(PluginCmd):
    author = "Rachid Chikh"
    version = "0.0.1"
    name = "PushCmd"
    hook = "badass.core.push"

    def preCmd(self, **kwargs):
        print "pre cmd:", kwargs

    def postCmd(self, **kwargs):
        print "post cmd:", kwargs


def initialize(**kwargs):
    plugin = PushCmd(**kwargs)
    return plugin
