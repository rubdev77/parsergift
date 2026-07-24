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


class UpdatePinnedForumTopic(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``223``
        - ID: ``175DF251``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            

        topic_id (``int`` ``32-bit``):
            

        pinned (``bool``):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "topic_id", "pinned"]

    ID = 0x175df251
    QUALNAME = "functions.messages.UpdatePinnedForumTopic"

    def __init__(self, *, peer: "raw.base.InputPeer", topic_id: int, pinned: bool) -> None:
        self.peer = peer  # InputPeer
        self.topic_id = topic_id  # int
        self.pinned = pinned  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopic":
        # No flags
        
        peer = TLObject.read(b)
        
        topic_id = Int.read(b)
        
        pinned = Bool.read(b)
        
        return UpdatePinnedForumTopic(peer=peer, topic_id=topic_id, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.topic_id))
        
        b.write(Bool(self.pinned))
        
        return b.getvalue()
