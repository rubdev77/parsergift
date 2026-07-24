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


class InputInvoiceStarGiftResale(TLObject):  # type: ignore
    """Used to buy a collectible gift currently up on resale, see here for more info on the full flow.

    Constructor of :obj:`~hydrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``223``
        - ID: ``C39F5324``

    Parameters:
        slug (``str``):
            Slug of the gift to buy.

        to_id (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The receiver of the gift.

        ton (``bool``, *optional*):
            Buy the gift using TON.

    """

    __slots__: List[str] = ["slug", "to_id", "ton"]

    ID = 0xc39f5324
    QUALNAME = "types.InputInvoiceStarGiftResale"

    def __init__(self, *, slug: str, to_id: "raw.base.InputPeer", ton: Optional[bool] = None) -> None:
        self.slug = slug  # string
        self.to_id = to_id  # InputPeer
        self.ton = ton  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftResale":
        
        flags = Int.read(b)
        
        ton = True if flags & (1 << 0) else False
        slug = String.read(b)
        
        to_id = TLObject.read(b)
        
        return InputInvoiceStarGiftResale(slug=slug, to_id=to_id, ton=ton)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        b.write(Int(flags))
        
        b.write(String(self.slug))
        
        b.write(self.to_id.write())
        
        return b.getvalue()
