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


class ReorderPinnedForumTopics(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``223``
        - ID: ``E7841F0``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            

        order (List of ``int`` ``32-bit``):
            

        force (``bool``, *optional*):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "order", "force"]

    ID = 0xe7841f0
    QUALNAME = "functions.messages.ReorderPinnedForumTopics"

    def __init__(self, *, peer: "raw.base.InputPeer", order: List[int], force: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.order = order  # Vector<int>
        self.force = force  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPinnedForumTopics":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        order = TLObject.read(b, Int)
        
        return ReorderPinnedForumTopics(peer=peer, order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.order, Int))
        
        return b.getvalue()
