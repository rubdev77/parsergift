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


class GroupCallMessage(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.GroupCallMessage`.

    Details:
        - Layer: ``223``
        - ID: ``1A8AFC7E``

    Parameters:
        id (``int`` ``32-bit``):
            

        from_id (:obj:`Peer <hydrogram.raw.base.Peer>`):
            

        date (``int`` ``32-bit``):
            

        message (:obj:`TextWithEntities <hydrogram.raw.base.TextWithEntities>`):
            

        from_admin (``bool``, *optional*):
            

        paid_message_stars (``int`` ``64-bit``, *optional*):
            

    """

    __slots__: List[str] = ["id", "from_id", "date", "message", "from_admin", "paid_message_stars"]

    ID = 0x1a8afc7e
    QUALNAME = "types.GroupCallMessage"

    def __init__(self, *, id: int, from_id: "raw.base.Peer", date: int, message: "raw.base.TextWithEntities", from_admin: Optional[bool] = None, paid_message_stars: Optional[int] = None) -> None:
        self.id = id  # int
        self.from_id = from_id  # Peer
        self.date = date  # int
        self.message = message  # TextWithEntities
        self.from_admin = from_admin  # flags.1?true
        self.paid_message_stars = paid_message_stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallMessage":
        
        flags = Int.read(b)
        
        from_admin = True if flags & (1 << 1) else False
        id = Int.read(b)
        
        from_id = TLObject.read(b)
        
        date = Int.read(b)
        
        message = TLObject.read(b)
        
        paid_message_stars = Long.read(b) if flags & (1 << 0) else None
        return GroupCallMessage(id=id, from_id=from_id, date=date, message=message, from_admin=from_admin, paid_message_stars=paid_message_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.from_admin else 0
        flags |= (1 << 0) if self.paid_message_stars is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(self.from_id.write())
        
        b.write(Int(self.date))
        
        b.write(self.message.write())
        
        if self.paid_message_stars is not None:
            b.write(Long(self.paid_message_stars))
        
        return b.getvalue()
