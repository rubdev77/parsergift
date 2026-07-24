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


class StarGiftAuctionRound(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.StarGiftAuctionRound`.

    Details:
        - Layer: ``223``
        - ID: ``3AAE0528``

    Parameters:
        num (``int`` ``32-bit``):
            

        duration (``int`` ``32-bit``):
            

    """

    __slots__: List[str] = ["num", "duration"]

    ID = 0x3aae0528
    QUALNAME = "types.StarGiftAuctionRound"

    def __init__(self, *, num: int, duration: int) -> None:
        self.num = num  # int
        self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionRound":
        # No flags
        
        num = Int.read(b)
        
        duration = Int.read(b)
        
        return StarGiftAuctionRound(num=num, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.num))
        
        b.write(Int(self.duration))
        
        return b.getvalue()
