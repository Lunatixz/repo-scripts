'''
    XBMC LCDproc addon
    Copyright (C) 2012-2018 Team Kodi

    resources/lib/common.py: Common defines and functionality used throughout
                             the whole addon
    Copyright (C) 2018 Daniel 'herrnst' Scheller

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os

import xbmc
import xbmcaddon

KODI_ADDON_ID       = "script.xbmc.lcdproc"
KODI_ADDON_NAME     = "XBMC LCDproc"
KODI_ADDON_SETTINGS = xbmcaddon.Addon(id=KODI_ADDON_ID)
KODI_ADDON_ROOTPATH = KODI_ADDON_SETTINGS.getAddonInfo("path")
KODI_ADDON_ICON     = os.path.join(KODI_ADDON_ROOTPATH, "resources", "icon.png")

# copy loglevel defines to the global scope
LOGDEBUG   = xbmc.LOGDEBUG
LOGERROR   = xbmc.LOGERROR
LOGFATAL   = xbmc.LOGFATAL
LOGINFO    = xbmc.LOGINFO
LOGNONE    = xbmc.LOGNONE
LOGWARNING = xbmc.LOGWARNING

# interesting Kodi GUI Window IDs (no defines seem to exist for this)
class WINDOW_IDS:
    WINDOW_WEATHER               = 12600
    WINDOW_PVR                   = 10601
    WINDOW_PVR_MAX               = 10799
    WINDOW_VIDEO_NAV             = 10025
    WINDOW_VIDEO_PLAYLIST        = 10028
    WINDOW_MUSIC_PLAYLIST        = 10500
    WINDOW_MUSIC_NAV             = 10502
    WINDOW_MUSIC_PLAYLIST_EDITOR = 10503
    WINDOW_PICTURES              = 10002
    WINDOW_DIALOG_VOLUME_BAR     = 10104
    WINDOW_DIALOG_KAI_TOAST	 = 10107

# log wrapper
def log(loglevel, msg):
	xbmc.log("### [%s] - %s" % (KODI_ADDON_NAME, msg), level=loglevel)
