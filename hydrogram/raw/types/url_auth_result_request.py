#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present Hydrogram <https://hydrogram.org>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from hydrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hydrogram.raw.core import TLObject
from hydrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UrlAuthResultRequest(TLObject):  # type: ignore
    """Details about the authorization request, for more info click here »

    Constructor of :obj:`~hydrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``223``
        - ID: ``F8F8EB1E``

    Parameters:
        bot (:obj:`User <hydrogram.raw.base.User>`):
            Username of a bot, which will be used for user authorization. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.

        domain (``str``):
            The domain name of the website on which the user will log in.

        request_write_access (``bool``, *optional*):
            Whether the bot would like to send messages to the user

        request_phone_number (``bool``, *optional*):
            

        match_codes_first (``bool``, *optional*):
            

        browser (``str``, *optional*):
            

        platform (``str``, *optional*):
            

        ip (``str``, *optional*):
            

        region (``str``, *optional*):
            

        match_codes (List of ``str``, *optional*):
            

        user_id_hint (``int`` ``64-bit``, *optional*):
            

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = ["bot", "domain", "request_write_access", "request_phone_number", "match_codes_first", "browser", "platform", "ip", "region", "match_codes", "user_id_hint"]

    ID = 0xf8f8eb1e
    QUALNAME = "types.UrlAuthResultRequest"

    def __init__(self, *, bot: "raw.base.User", domain: str, request_write_access: Optional[bool] = None, request_phone_number: Optional[bool] = None, match_codes_first: Optional[bool] = None, browser: Optional[str] = None, platform: Optional[str] = None, ip: Optional[str] = None, region: Optional[str] = None, match_codes: Optional[List[str]] = None, user_id_hint: Optional[int] = None) -> None:
        self.bot = bot  # User
        self.domain = domain  # string
        self.request_write_access = request_write_access  # flags.0?true
        self.request_phone_number = request_phone_number  # flags.1?true
        self.match_codes_first = match_codes_first  # flags.5?true
        self.browser = browser  # flags.2?string
        self.platform = platform  # flags.2?string
        self.ip = ip  # flags.2?string
        self.region = region  # flags.2?string
        self.match_codes = match_codes  # flags.3?Vector<string>
        self.user_id_hint = user_id_hint  # flags.4?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultRequest":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        request_phone_number = True if flags & (1 << 1) else False
        match_codes_first = True if flags & (1 << 5) else False
        bot = TLObject.read(b)
        
        domain = String.read(b)
        
        browser = String.read(b) if flags & (1 << 2) else None
        platform = String.read(b) if flags & (1 << 2) else None
        ip = String.read(b) if flags & (1 << 2) else None
        region = String.read(b) if flags & (1 << 2) else None
        match_codes = TLObject.read(b, String) if flags & (1 << 3) else []
        
        user_id_hint = Long.read(b) if flags & (1 << 4) else None
        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access, request_phone_number=request_phone_number, match_codes_first=match_codes_first, browser=browser, platform=platform, ip=ip, region=region, match_codes=match_codes, user_id_hint=user_id_hint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.request_phone_number else 0
        flags |= (1 << 5) if self.match_codes_first else 0
        flags |= (1 << 2) if self.browser is not None else 0
        flags |= (1 << 2) if self.platform is not None else 0
        flags |= (1 << 2) if self.ip is not None else 0
        flags |= (1 << 2) if self.region is not None else 0
        flags |= (1 << 3) if self.match_codes else 0
        flags |= (1 << 4) if self.user_id_hint is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(String(self.domain))
        
        if self.browser is not None:
            b.write(String(self.browser))
        
        if self.platform is not None:
            b.write(String(self.platform))
        
        if self.ip is not None:
            b.write(String(self.ip))
        
        if self.region is not None:
            b.write(String(self.region))
        
        if self.match_codes is not None:
            b.write(Vector(self.match_codes, String))
        
        if self.user_id_hint is not None:
            b.write(Long(self.user_id_hint))
        
        return b.getvalue()
