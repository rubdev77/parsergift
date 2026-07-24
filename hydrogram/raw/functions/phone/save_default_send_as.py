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


class SaveDefaultSendAs(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``223``
        - ID: ``4167ADD1``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            

        send_as (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["call", "send_as"]

    ID = 0x4167add1
    QUALNAME = "functions.phone.SaveDefaultSendAs"

    def __init__(self, *, call: "raw.base.InputGroupCall", send_as: "raw.base.InputPeer") -> None:
        self.call = call  # InputGroupCall
        self.send_as = send_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveDefaultSendAs":
        # No flags
        
        call = TLObject.read(b)
        
        send_as = TLObject.read(b)
        
        return SaveDefaultSendAs(call=call, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(self.send_as.write())
        
        return b.getvalue()
