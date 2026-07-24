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


class MessageMediaToDo(TLObject):  # type: ignore
    """Represents a todo list ».

    Constructor of :obj:`~hydrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``223``
        - ID: ``8A53B014``

    Parameters:
        todo (:obj:`TodoList <hydrogram.raw.base.TodoList>`):
            The todo list.

        completions (List of :obj:`TodoCompletion <hydrogram.raw.base.TodoCompletion>`, *optional*):
            Completed items.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["todo", "completions"]

    ID = 0x8a53b014
    QUALNAME = "types.MessageMediaToDo"

    def __init__(self, *, todo: "raw.base.TodoList", completions: Optional[List["raw.base.TodoCompletion"]] = None) -> None:
        self.todo = todo  # TodoList
        self.completions = completions  # flags.0?Vector<TodoCompletion>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaToDo":
        
        flags = Int.read(b)
        
        todo = TLObject.read(b)
        
        completions = TLObject.read(b) if flags & (1 << 0) else []
        
        return MessageMediaToDo(todo=todo, completions=completions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.completions else 0
        b.write(Int(flags))
        
        b.write(self.todo.write())
        
        if self.completions is not None:
            b.write(Vector(self.completions))
        
        return b.getvalue()
