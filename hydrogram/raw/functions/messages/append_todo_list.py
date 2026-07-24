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


class AppendTodoList(TLObject):  # type: ignore
    """Appends one or more items to a todo list ».


    Details:
        - Layer: ``223``
        - ID: ``21A61057``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where the todo list was posted.

        msg_id (``int`` ``32-bit``):
            ID of the message with the todo list.

        list (List of :obj:`TodoItem <hydrogram.raw.base.TodoItem>`):
            Items to append.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "list"]

    ID = 0x21a61057
    QUALNAME = "functions.messages.AppendTodoList"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, list: List["raw.base.TodoItem"]) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.list = list  # Vector<TodoItem>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppendTodoList":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        list = TLObject.read(b)
        
        return AppendTodoList(peer=peer, msg_id=msg_id, list=list)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Vector(self.list))
        
        return b.getvalue()
