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


class ChannelAdminLogEventActionParticipantEditRank(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``223``
        - ID: ``5806B4EC``

    Parameters:
        user_id (``int`` ``64-bit``):
            

        prev_rank (``str``):
            

        new_rank (``str``):
            

    """

    __slots__: List[str] = ["user_id", "prev_rank", "new_rank"]

    ID = 0x5806b4ec
    QUALNAME = "types.ChannelAdminLogEventActionParticipantEditRank"

    def __init__(self, *, user_id: int, prev_rank: str, new_rank: str) -> None:
        self.user_id = user_id  # long
        self.prev_rank = prev_rank  # string
        self.new_rank = new_rank  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantEditRank":
        # No flags
        
        user_id = Long.read(b)
        
        prev_rank = String.read(b)
        
        new_rank = String.read(b)
        
        return ChannelAdminLogEventActionParticipantEditRank(user_id=user_id, prev_rank=prev_rank, new_rank=new_rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.prev_rank))
        
        b.write(String(self.new_rank))
        
        return b.getvalue()
