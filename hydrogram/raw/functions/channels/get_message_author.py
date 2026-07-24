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


class GetMessageAuthor(TLObject):  # type: ignore
    """Can only be invoked by non-bot admins of a monoforum », obtains the original sender of a message sent by other monoforum admins to the monoforum, on behalf of the channel associated to the monoforum.


    Details:
        - Layer: ``223``
        - ID: ``ECE2A0E6``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            ID of the monoforum.

        id (``int`` ``32-bit``):
            ID of the message sent by a monoforum admin.

    Returns:
        :obj:`User <hydrogram.raw.base.User>`
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0xece2a0e6
    QUALNAME = "functions.channels.GetMessageAuthor"

    def __init__(self, *, channel: "raw.base.InputChannel", id: int) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageAuthor":
        # No flags
        
        channel = TLObject.read(b)
        
        id = Int.read(b)
        
        return GetMessageAuthor(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
