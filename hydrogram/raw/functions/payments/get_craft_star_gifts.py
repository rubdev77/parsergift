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


class GetCraftStarGifts(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``223``
        - ID: ``FD05DD00``

    Parameters:
        gift_id (``int`` ``64-bit``):
            

        offset (``str``):
            

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

    Returns:
        :obj:`payments.SavedStarGifts <hydrogram.raw.base.payments.SavedStarGifts>`
    """

    __slots__: List[str] = ["gift_id", "offset", "limit"]

    ID = 0xfd05dd00
    QUALNAME = "functions.payments.GetCraftStarGifts"

    def __init__(self, *, gift_id: int, offset: str, limit: int) -> None:
        self.gift_id = gift_id  # long
        self.offset = offset  # string
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCraftStarGifts":
        # No flags
        
        gift_id = Long.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetCraftStarGifts(gift_id=gift_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.gift_id))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
