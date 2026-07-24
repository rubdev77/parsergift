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


class WebPagePreview(TLObject):  # type: ignore
    """Represents a webpage preview.

    Constructor of :obj:`~hydrogram.raw.base.messages.WebPagePreview`.

    Details:
        - Layer: ``223``
        - ID: ``8C9A88AC``

    Parameters:
        media (:obj:`MessageMedia <hydrogram.raw.base.MessageMedia>`):
            The messageMediaWebPage or a messageMediaEmpty if there is no preview.

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Chats mentioned in the gift field.

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users mentioned within the media object.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
    """

    __slots__: List[str] = ["media", "chats", "users"]

    ID = 0x8c9a88ac
    QUALNAME = "types.messages.WebPagePreview"

    def __init__(self, *, media: "raw.base.MessageMedia", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.media = media  # MessageMedia
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPagePreview":
        # No flags
        
        media = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return WebPagePreview(media=media, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.media.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
