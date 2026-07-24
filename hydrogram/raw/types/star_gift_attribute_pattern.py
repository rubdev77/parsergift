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


class StarGiftAttributePattern(TLObject):  # type: ignore
    """A sticker applied on the backdrop of a collectible gift » using a repeating pattern.

    Constructor of :obj:`~hydrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``223``
        - ID: ``4E7085EA``

    Parameters:
        name (``str``):
            Name of the symbol

        document (:obj:`Document <hydrogram.raw.base.Document>`):
            The symbol

        rarity (:obj:`StarGiftAttributeRarity <hydrogram.raw.base.StarGiftAttributeRarity>`):
            

    """

    __slots__: List[str] = ["name", "document", "rarity"]

    ID = 0x4e7085ea
    QUALNAME = "types.StarGiftAttributePattern"

    def __init__(self, *, name: str, document: "raw.base.Document", rarity: "raw.base.StarGiftAttributeRarity") -> None:
        self.name = name  # string
        self.document = document  # Document
        self.rarity = rarity  # StarGiftAttributeRarity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributePattern":
        # No flags
        
        name = String.read(b)
        
        document = TLObject.read(b)
        
        rarity = TLObject.read(b)
        
        return StarGiftAttributePattern(name=name, document=document, rarity=rarity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.name))
        
        b.write(self.document.write())
        
        b.write(self.rarity.write())
        
        return b.getvalue()
