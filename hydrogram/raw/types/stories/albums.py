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


class Albums(TLObject):  # type: ignore
    """Story albums ».

    Constructor of :obj:`~hydrogram.raw.base.stories.Albums`.

    Details:
        - Layer: ``223``
        - ID: ``C3987A3A``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash to pass to stories.getAlbums to avoid returning any results if they haven't changed.

        albums (List of :obj:`StoryAlbum <hydrogram.raw.base.StoryAlbum>`):
            The albums.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAlbums
    """

    __slots__: List[str] = ["hash", "albums"]

    ID = 0xc3987a3a
    QUALNAME = "types.stories.Albums"

    def __init__(self, *, hash: int, albums: List["raw.base.StoryAlbum"]) -> None:
        self.hash = hash  # long
        self.albums = albums  # Vector<StoryAlbum>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Albums":
        # No flags
        
        hash = Long.read(b)
        
        albums = TLObject.read(b)
        
        return Albums(hash=hash, albums=albums)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.albums))
        
        return b.getvalue()
