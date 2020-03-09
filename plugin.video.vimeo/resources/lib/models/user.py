from future import standard_library
standard_library.install_aliases()  # noqa: E402

from resources.lib.models.list_item import ListItem
import urllib.parse
import xbmcgui


class User(ListItem):
    thumb = ""
    info = {}
    uri = ""

    def to_list_item(self, addon, addon_base):
        list_item = xbmcgui.ListItem(label=self.label, label2=self.label2)
        list_item.setArt({"thumb": self.thumb})
        list_item.setInfo("video", {
            "country": self.info.get("country"),
            "title": self.info.get("description"),
            "year": self.info.get("date")[:4]
        })
        url = addon_base + "/?" + urllib.parse.urlencode({
            "action": "call",
            "call": self.uri
        })

        return url, list_item, True