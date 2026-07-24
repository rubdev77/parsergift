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


class InviteConferenceCallParticipant(TLObject):  # type: ignore
    """Invite a user to a conference call.


    Details:
        - Layer: ``223``
        - ID: ``BCF22685``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            The conference call.

        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            The user to invite.

        video (``bool``, *optional*):
            Invite the user to also turn on their video feed.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "user_id", "video"]

    ID = 0xbcf22685
    QUALNAME = "functions.phone.InviteConferenceCallParticipant"

    def __init__(self, *, call: "raw.base.InputGroupCall", user_id: "raw.base.InputUser", video: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.user_id = user_id  # InputUser
        self.video = video  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteConferenceCallParticipant":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return InviteConferenceCallParticipant(call=call, user_id=user_id, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
