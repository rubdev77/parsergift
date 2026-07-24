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


class InputInvoiceBusinessBotTransferStars(TLObject):  # type: ignore
    """Transfer stars from the balance of a user account connected to a business bot, to the balance of the business bot, see here » for more info on the full flow.

    Constructor of :obj:`~hydrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``223``
        - ID: ``F4997E42``

    Parameters:
        bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Always inputUserSelf.

        stars (``int`` ``64-bit``):
            The number of stars to transfer.

    """

    __slots__: List[str] = ["bot", "stars"]

    ID = 0xf4997e42
    QUALNAME = "types.InputInvoiceBusinessBotTransferStars"

    def __init__(self, *, bot: "raw.base.InputUser", stars: int) -> None:
        self.bot = bot  # InputUser
        self.stars = stars  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceBusinessBotTransferStars":
        # No flags
        
        bot = TLObject.read(b)
        
        stars = Long.read(b)
        
        return InputInvoiceBusinessBotTransferStars(bot=bot, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Long(self.stars))
        
        return b.getvalue()
