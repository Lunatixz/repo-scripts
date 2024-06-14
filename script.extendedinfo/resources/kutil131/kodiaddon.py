# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

import base64
import hashlib
import os
import uuid

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

HOME = xbmcgui.Window(10000)


class Addon:
    """
    Wrapper for xbmcaddon.Addon()
    """

    def __init__(self, *args, **kwargs):
        self.addon = xbmcaddon.Addon(*args)
        self.ID = self.addon.getAddonInfo('id')
        self.ICON = self.addon.getAddonInfo('icon')
        self.NAME = self.addon.getAddonInfo('name')
        self.FANART = self.addon.getAddonInfo('fanart')
        self.AUTHOR = self.addon.getAddonInfo('author')
        self.CHANGELOG = self.addon.getAddonInfo('changelog')
        self.DESCRIPTION = self.addon.getAddonInfo('description')
        self.DISCLAIMER = self.addon.getAddonInfo('disclaimer')
        self.VERSION = self.addon.getAddonInfo('version')
        self.PATH = self.addon.getAddonInfo('path')
        self.PROFILE = self.addon.getAddonInfo('profile')
        self.SUMMARY = self.addon.getAddonInfo('summary')
        self.TYPE = self.addon.getAddonInfo('type')
        self.MEDIA_PATH = os.path.join(self.PATH, "resources", "skins", "Default", "media")
        self.DATA_PATH = xbmcvfs.translatePath("special://profile/addon_data/%s" % self.ID)

    def setting(self, setting_name):
        """
        get setting with name *setting_name
        """
        return self.addon.getSetting(setting_name)

    def set_setting(self, setting_name, string):
        """
        set setting with name *setting_name to value *string
        """
        self.addon.setSetting(str(setting_name), str(string))

    def set_password_prompt(self, setting_name):
        password = xbmcgui.Dialog().input(self.LANG(12326), option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if password:
            self.set_password(setting_name, password)

    def set_password(self, setting_name, string):
        self.addon.setSetting(setting_name, encode_string(string))

    def get_password(self, setting_name):
        mac = str(uuid.getnode())
        mac_hash = hashlib.md5(mac.encode()).hexdigest()
        if not self.addon.getSetting("mac_hash"):
            self.addon.setSetting("mac_hash", mac_hash)
        elif self.addon.getSetting("mac_hash") != mac_hash:
            xbmcgui.Dialog().notification("Error", "MAC id changed. Please enter password again in settings.")
            self.addon.setSetting("mac_hash", mac_hash)
            return None
        setting = self.addon.getSetting(setting_name)
        if setting:
            return decode_string(setting)

    def bool_setting(self, setting_name):
        """
        get bool setting (either True or False)
        """
        return self.addon.getSetting(setting_name) == "true"

    def reload_addon(self):
        self.addon = xbmcaddon.Addon(self.ID)

    def LANG(self, id_):
        return self.addon.getLocalizedString(id_) if 31000 <= id_ <= 33000 else xbmc.getLocalizedString(id_)

    def set_global(self, setting_name: str, setting_value: str) ->None:
        """sets xbmc Window SetProperty(setting_name,setting_value,home)

        Args:
            setting_name (str): property key
            setting_value (str): property value
        """
        HOME.setProperty(setting_name, setting_value)

    def get_global(self, setting_name):
        return HOME.getProperty(setting_name)

    def clear_global(self, setting_name):
        HOME.clearProperty(setting_name)

    def clear_globals(self):
        HOME.clearProperties()


def encode_string(clear: str) -> str:
    """base64 encodes a string

    Args:
        clear (str): string to be encoded

    Returns:
        str: the url safe base64 encoding as bytes
    """
    enc = []
    key = str(uuid.getnode())
    clear_enc = clear.encode()
    for i, ele in enumerate(clear_enc):
        key_c = key[i % len(key)]
        enc_c = chr((ele + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode_string(enc: str, uuick: str='') -> str:
    """return decoded string (encoded with uuid)

    Args:
        enc (str): base64 string encoded by encode_string
    
    Returns:
        str:  the decoded string
    """
    dec = []
    key = str(uuid.getnode()) if not uuick else uuick
    enc = base64.urlsafe_b64decode(enc.encode()).decode()
    for i, ele in enumerate(enc):
        key_c = key[i % len(key)]
        dec_c = ((256 + ord(ele) - ord(key_c)) % 256).to_bytes(1, 'little')
        dec.append(dec_c)
    return bytes.join(b'', dec).decode()