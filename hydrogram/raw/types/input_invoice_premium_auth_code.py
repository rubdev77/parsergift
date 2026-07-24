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


class InputInvoicePremiumAuthCode(TLObject):  # type: ignore
    """Used to pay for login codes, in case of high cost of SMS verification codes for the user's country/provider, see here » for more info.

    Constructor of :obj:`~hydrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``223``
        - ID: ``3E77F614``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <hydrogram.raw.base.InputStorePaymentPurpose>`):
            Must contain an inputStorePaymentAuthCode.

    """

    __slots__: List[str] = ["purpose"]

    ID = 0x3e77f614
    QUALNAME = "types.InputInvoicePremiumAuthCode"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumAuthCode":
        # No flags
        
        purpose = TLObject.read(b)
        
        return InputInvoicePremiumAuthCode(purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        return b.getvalue()
