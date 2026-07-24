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


class InputInvoicePremiumGiftStars(TLObject):  # type: ignore
    """Used to gift a Telegram Premium subscription to another user, paying with Telegram Stars.

    Constructor of :obj:`~hydrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``223``
        - ID: ``DABAB2EF``

    Parameters:
        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Who will receive the gifted subscription.

        months (``int`` ``32-bit``):
            Duration of the subscription in months, must be one of the options with currency == "XTR" returned by payments.getPremiumGiftCodeOptions.

        message (:obj:`TextWithEntities <hydrogram.raw.base.TextWithEntities>`, *optional*):
            Message attached with the gift.

    """

    __slots__: List[str] = ["user_id", "months", "message"]

    ID = 0xdabab2ef
    QUALNAME = "types.InputInvoicePremiumGiftStars"

    def __init__(self, *, user_id: "raw.base.InputUser", months: int, message: "raw.base.TextWithEntities" = None) -> None:
        self.user_id = user_id  # InputUser
        self.months = months  # int
        self.message = message  # flags.0?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumGiftStars":
        
        flags = Int.read(b)
        
        user_id = TLObject.read(b)
        
        months = Int.read(b)
        
        message = TLObject.read(b) if flags & (1 << 0) else None
        
        return InputInvoicePremiumGiftStars(user_id=user_id, months=months, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message is not None else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.months))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
