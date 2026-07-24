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


class TodoCompletion(TLObject):  # type: ignore
    """A completed todo list » item.

    Constructor of :obj:`~hydrogram.raw.base.TodoCompletion`.

    Details:
        - Layer: ``223``
        - ID: ``221BB5E4``

    Parameters:
        id (``int`` ``32-bit``):
            The ID of the completed item.

        completed_by (:obj:`Peer <hydrogram.raw.base.Peer>`):
            ID of the user that completed the item.

        date (``int`` ``32-bit``):
            When was the item completed.

    """

    __slots__: List[str] = ["id", "completed_by", "date"]

    ID = 0x221bb5e4
    QUALNAME = "types.TodoCompletion"

    def __init__(self, *, id: int, completed_by: "raw.base.Peer", date: int) -> None:
        self.id = id  # int
        self.completed_by = completed_by  # Peer
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TodoCompletion":
        # No flags
        
        id = Int.read(b)
        
        completed_by = TLObject.read(b)
        
        date = Int.read(b)
        
        return TodoCompletion(id=id, completed_by=completed_by, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(self.completed_by.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
