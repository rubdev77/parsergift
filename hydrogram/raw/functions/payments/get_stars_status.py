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


class GetStarsStatus(TLObject):  # type: ignore
    """Get the current Telegram Stars balance of the current account (with peer=inputPeerSelf), or the stars balance of the bot specified in peer.


    Details:
        - Layer: ``223``
        - ID: ``4EA9B3BF``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer of which to get the balance.

        ton (``bool``, *optional*):
            If set, returns the channel/ad revenue balance in nanotons.

    Returns:
        :obj:`payments.StarsStatus <hydrogram.raw.base.payments.StarsStatus>`
    """

    __slots__: List[str] = ["peer", "ton"]

    ID = 0x4ea9b3bf
    QUALNAME = "functions.payments.GetStarsStatus"

    def __init__(self, *, peer: "raw.base.InputPeer", ton: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.ton = ton  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsStatus":
        
        flags = Int.read(b)
        
        ton = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return GetStarsStatus(peer=peer, ton=ton)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
