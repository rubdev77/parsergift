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


class EditChatCreator(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``223``
        - ID: ``F743B857``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            

        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            

        password (:obj:`InputCheckPasswordSRP <hydrogram.raw.base.InputCheckPasswordSRP>`):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "user_id", "password"]

    ID = 0xf743b857
    QUALNAME = "functions.messages.EditChatCreator"

    def __init__(self, *, peer: "raw.base.InputPeer", user_id: "raw.base.InputUser", password: "raw.base.InputCheckPasswordSRP") -> None:
        self.peer = peer  # InputPeer
        self.user_id = user_id  # InputUser
        self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatCreator":
        # No flags
        
        peer = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        password = TLObject.read(b)
        
        return EditChatCreator(peer=peer, user_id=user_id, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.user_id.write())
        
        b.write(self.password.write())
        
        return b.getvalue()
