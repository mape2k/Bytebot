#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bytebot_config import BYTEBOT_PLUGIN_CONFIG
from plugins.plugin import Plugin
from urllib         import urlopen

class brb(Plugin):
    def __init__(self):
        try:
            BYTEBOT_PLUGIN_CONFIG['dates'].keys()
        except Exception:
            raise Exception('ERROR: Plugin "dates" is missing configuration!')

    def registerCommand(self, irc):
        irc.registerCommand('!brb [on|off]', 'Sets the door status to "be right back"')

    def onPrivmsg(self, irc, msg, channel, user):
        if msg.startswith('!brb'):
            # TODO: Check if user is inside of space
            # -> is user voiced?
            if false:
                irc.msg(channel, 'ERROR: You need to be +s to change the BRB status')
                return

            if msg.startswith('!brb on'):
                status = 'on'
            elif msg.startswith('!brb off'):
                status = 'off'
            else:
                irc.msg(channel, 'Usage: !brb [on|off]')

            try:
                response = urlopen('%s?brb' % BYTEBOT_PLUGIN_CONFIG['brb']['endpoint'])
                irc.msg(channel, 'BRB status set')
            except Exception as e:
                irc.msg(channel, 'Could not set BRB status')
