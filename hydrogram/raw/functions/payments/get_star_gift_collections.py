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


class GetStarGiftCollections(TLObject):  # type: ignore
    """Fetches all star gift collections » of a peer.


    Details:
        - Layer: ``223``
        - ID: ``981B91DD``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The peer.

        hash (``int`` ``64-bit``):
            Hash (generated as specified here ») using the starGiftCollection.hash field (not the collection_id field) of all collections returned by a previous method call, to avoid refetching the result if it hasn't changed.

    Returns:
        :obj:`payments.StarGiftCollections <hydrogram.raw.base.payments.StarGiftCollections>`
    """

    __slots__: List[str] = ["peer", "hash"]

    ID = 0x981b91dd
    QUALNAME = "functions.payments.GetStarGiftCollections"

    def __init__(self, *, peer: "raw.base.InputPeer", hash: int) -> None:
        self.peer = peer  # InputPeer
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftCollections":
        # No flags
        
        peer = TLObject.read(b)
        
        hash = Long.read(b)
        
        return GetStarGiftCollections(peer=peer, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()
