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


class GroupCallStars(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.phone.GroupCallStars`.

    Details:
        - Layer: ``223``
        - ID: ``9D1DBD26``

    Parameters:
        total_stars (``int`` ``64-bit``):
            

        top_donors (List of :obj:`GroupCallDonor <hydrogram.raw.base.GroupCallDonor>`):
            

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStars
    """

    __slots__: List[str] = ["total_stars", "top_donors", "chats", "users"]

    ID = 0x9d1dbd26
    QUALNAME = "types.phone.GroupCallStars"

    def __init__(self, *, total_stars: int, top_donors: List["raw.base.GroupCallDonor"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.total_stars = total_stars  # long
        self.top_donors = top_donors  # Vector<GroupCallDonor>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStars":
        # No flags
        
        total_stars = Long.read(b)
        
        top_donors = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return GroupCallStars(total_stars=total_stars, top_donors=top_donors, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.total_stars))
        
        b.write(Vector(self.top_donors))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
