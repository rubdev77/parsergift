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


class WebPageAttributeStarGiftCollection(TLObject):  # type: ignore
    """Contains info about a gift collection » for a webPage preview of a gift collection » (the webPage will have a type of telegram_collection).

    Constructor of :obj:`~hydrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``223``
        - ID: ``31CAD303``

    Parameters:
        icons (List of :obj:`Document <hydrogram.raw.base.Document>`):
            Gifts in the collection.

    """

    __slots__: List[str] = ["icons"]

    ID = 0x31cad303
    QUALNAME = "types.WebPageAttributeStarGiftCollection"

    def __init__(self, *, icons: List["raw.base.Document"]) -> None:
        self.icons = icons  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStarGiftCollection":
        # No flags
        
        icons = TLObject.read(b)
        
        return WebPageAttributeStarGiftCollection(icons=icons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.icons))
        
        return b.getvalue()
