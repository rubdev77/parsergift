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


class MessageActionNoForwardsRequest(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``223``
        - ID: ``3E2793BA``

    Parameters:
        prev_value (``bool``):
            

        new_value (``bool``):
            

        expired (``bool``, *optional*):
            

    """

    __slots__: List[str] = ["prev_value", "new_value", "expired"]

    ID = 0x3e2793ba
    QUALNAME = "types.MessageActionNoForwardsRequest"

    def __init__(self, *, prev_value: bool, new_value: bool, expired: Optional[bool] = None) -> None:
        self.prev_value = prev_value  # Bool
        self.new_value = new_value  # Bool
        self.expired = expired  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionNoForwardsRequest":
        
        flags = Int.read(b)
        
        expired = True if flags & (1 << 0) else False
        prev_value = Bool.read(b)
        
        new_value = Bool.read(b)
        
        return MessageActionNoForwardsRequest(prev_value=prev_value, new_value=new_value, expired=expired)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.expired else 0
        b.write(Int(flags))
        
        b.write(Bool(self.prev_value))
        
        b.write(Bool(self.new_value))
        
        return b.getvalue()
