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


class UpdateStarGiftPrice(TLObject):  # type: ignore
    """A collectible gift we own » can be put up for sale on the gift marketplace » with this method, see here » for more info.


    Details:
        - Layer: ``223``
        - ID: ``EDBE6CCB``

    Parameters:
        stargift (:obj:`InputSavedStarGift <hydrogram.raw.base.InputSavedStarGift>`):
            The gift to resell.

        resell_amount (:obj:`StarsAmount <hydrogram.raw.base.StarsAmount>`):
            Resale price of the gift.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["stargift", "resell_amount"]

    ID = 0xedbe6ccb
    QUALNAME = "functions.payments.UpdateStarGiftPrice"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", resell_amount: "raw.base.StarsAmount") -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.resell_amount = resell_amount  # StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftPrice":
        # No flags
        
        stargift = TLObject.read(b)
        
        resell_amount = TLObject.read(b)
        
        return UpdateStarGiftPrice(stargift=stargift, resell_amount=resell_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stargift.write())
        
        b.write(self.resell_amount.write())
        
        return b.getvalue()
