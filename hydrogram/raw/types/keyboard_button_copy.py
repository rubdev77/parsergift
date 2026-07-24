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


class KeyboardButtonCopy(TLObject):  # type: ignore
    """Clipboard button: when clicked, the attached text must be copied to the clipboard.

    Constructor of :obj:`~hydrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``223``
        - ID: ``BCC4AF10``

    Parameters:
        text (``str``):
            Title of the button

        copy_text (``str``):
            The text that will be copied to the clipboard

        style (:obj:`KeyboardButtonStyle <hydrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            

    """

    __slots__: List[str] = ["text", "copy_text", "style"]

    ID = 0xbcc4af10
    QUALNAME = "types.KeyboardButtonCopy"

    def __init__(self, *, text: str, copy_text: str, style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text  # string
        self.copy_text = copy_text  # string
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCopy":
        
        flags = Int.read(b)
        
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        copy_text = String.read(b)
        
        return KeyboardButtonCopy(text=text, copy_text=copy_text, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        b.write(String(self.copy_text))
        
        return b.getvalue()
