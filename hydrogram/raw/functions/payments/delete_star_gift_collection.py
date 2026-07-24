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


class DeleteStarGiftCollection(TLObject):  # type: ignore
    """Delete a star gift collection ».


    Details:
        - Layer: ``223``
        - ID: ``AD5648E8``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer that owns the collection.

        collection_id (``int`` ``32-bit``):
            ID of the collection.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "collection_id"]

    ID = 0xad5648e8
    QUALNAME = "functions.payments.DeleteStarGiftCollection"

    def __init__(self, *, peer: "raw.base.InputPeer", collection_id: int) -> None:
        self.peer = peer  # InputPeer
        self.collection_id = collection_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStarGiftCollection":
        # No flags
        
        peer = TLObject.read(b)
        
        collection_id = Int.read(b)
        
        return DeleteStarGiftCollection(peer=peer, collection_id=collection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.collection_id))
        
        return b.getvalue()
