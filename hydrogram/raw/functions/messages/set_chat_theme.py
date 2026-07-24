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


class SetChatTheme(TLObject):  # type: ignore
    """Change the chat theme of a certain chat, see here » for more info.


    Details:
        - Layer: ``223``
        - ID: ``81202C9``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Private chat where to change theme

        theme (:obj:`InputChatTheme <hydrogram.raw.base.InputChatTheme>`):
            The theme to set.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "theme"]

    ID = 0x81202c9
    QUALNAME = "functions.messages.SetChatTheme"

    def __init__(self, *, peer: "raw.base.InputPeer", theme: "raw.base.InputChatTheme") -> None:
        self.peer = peer  # InputPeer
        self.theme = theme  # InputChatTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatTheme":
        # No flags
        
        peer = TLObject.read(b)
        
        theme = TLObject.read(b)
        
        return SetChatTheme(peer=peer, theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.theme.write())
        
        return b.getvalue()
