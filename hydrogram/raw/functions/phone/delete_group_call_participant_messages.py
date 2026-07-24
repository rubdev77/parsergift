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


class DeleteGroupCallParticipantMessages(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``223``
        - ID: ``1DBFECA0``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            

        participant (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            

        report_spam (``bool``, *optional*):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "participant", "report_spam"]

    ID = 0x1dbfeca0
    QUALNAME = "functions.phone.DeleteGroupCallParticipantMessages"

    def __init__(self, *, call: "raw.base.InputGroupCall", participant: "raw.base.InputPeer", report_spam: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.participant = participant  # InputPeer
        self.report_spam = report_spam  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteGroupCallParticipantMessages":
        
        flags = Int.read(b)
        
        report_spam = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        return DeleteGroupCallParticipantMessages(call=call, participant=participant, report_spam=report_spam)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()
