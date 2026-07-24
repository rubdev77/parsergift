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


class MessageActionStarGiftPurchaseOfferDeclined(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``223``
        - ID: ``73ADA76B``

    Parameters:
        gift (:obj:`StarGift <hydrogram.raw.base.StarGift>`):
            

        price (:obj:`StarsAmount <hydrogram.raw.base.StarsAmount>`):
            

        expired (``bool``, *optional*):
            

    """

    __slots__: List[str] = ["gift", "price", "expired"]

    ID = 0x73ada76b
    QUALNAME = "types.MessageActionStarGiftPurchaseOfferDeclined"

    def __init__(self, *, gift: "raw.base.StarGift", price: "raw.base.StarsAmount", expired: Optional[bool] = None) -> None:
        self.gift = gift  # StarGift
        self.price = price  # StarsAmount
        self.expired = expired  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionStarGiftPurchaseOfferDeclined":
        
        flags = Int.read(b)
        
        expired = True if flags & (1 << 0) else False
        gift = TLObject.read(b)
        
        price = TLObject.read(b)
        
        return MessageActionStarGiftPurchaseOfferDeclined(gift=gift, price=price, expired=expired)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.expired else 0
        b.write(Int(flags))
        
        b.write(self.gift.write())
        
        b.write(self.price.write())
        
        return b.getvalue()
