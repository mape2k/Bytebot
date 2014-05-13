#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re

from plugins.plugin import Plugin

class replace(Plugin):
    def __init__(self):
        pass

    def onPrivmsg(self, irc, msg, channel, user):
        if msg.startswith('s/') == -1:
            return
