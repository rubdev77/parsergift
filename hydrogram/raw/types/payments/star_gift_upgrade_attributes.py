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


class StarGiftUpgradeAttributes(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.payments.StarGiftUpgradeAttributes`.

    Details:
        - Layer: ``223``
        - ID: ``46C6E36F``

    Parameters:
        attributes (List of :obj:`StarGiftAttribute <hydrogram.raw.base.StarGiftAttribute>`):
            

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftUpgradeAttributes
    """

    __slots__: List[str] = ["attributes"]

    ID = 0x46c6e36f
    QUALNAME = "types.payments.StarGiftUpgradeAttributes"

    def __init__(self, *, attributes: List["raw.base.StarGiftAttribute"]) -> None:
        self.attributes = attributes  # Vector<StarGiftAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUpgradeAttributes":
        # No flags
        
        attributes = TLObject.read(b)
        
        return StarGiftUpgradeAttributes(attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.attributes))
        
        return b.getvalue()
