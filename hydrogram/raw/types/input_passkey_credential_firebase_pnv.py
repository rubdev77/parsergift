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


class InputPasskeyCredentialFirebasePNV(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.InputPasskeyCredential`.

    Details:
        - Layer: ``223``
        - ID: ``5B1CCB28``

    Parameters:
        pnv_token (``str``):
            

    """

    __slots__: List[str] = ["pnv_token"]

    ID = 0x5b1ccb28
    QUALNAME = "types.InputPasskeyCredentialFirebasePNV"

    def __init__(self, *, pnv_token: str) -> None:
        self.pnv_token = pnv_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPasskeyCredentialFirebasePNV":
        # No flags
        
        pnv_token = String.read(b)
        
        return InputPasskeyCredentialFirebasePNV(pnv_token=pnv_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.pnv_token))
        
        return b.getvalue()
