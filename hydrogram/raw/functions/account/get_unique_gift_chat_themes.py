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


class GetUniqueGiftChatThemes(TLObject):  # type: ignore
    """Obtain all chat themes » associated to owned collectible gifts ».


    Details:
        - Layer: ``223``
        - ID: ``E42CE9C9``

    Parameters:
        offset (``str``):
            Offset for pagination.

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        hash (``int`` ``64-bit``):
            Hash from a previously returned account.chatThemes constructor, to avoid returning any result if the theme list hasn't changed.

    Returns:
        :obj:`account.ChatThemes <hydrogram.raw.base.account.ChatThemes>`
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0xe42ce9c9
    QUALNAME = "functions.account.GetUniqueGiftChatThemes"

    def __init__(self, *, offset: str, limit: int, hash: int) -> None:
        self.offset = offset  # string
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUniqueGiftChatThemes":
        # No flags
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetUniqueGiftChatThemes(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
