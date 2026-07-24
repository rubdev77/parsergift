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


class InputPeerColorCollectible(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.PeerColor`.

    Details:
        - Layer: ``223``
        - ID: ``B8EA86A9``

    Parameters:
        collectible_id (``int`` ``64-bit``):
            

    """

    __slots__: List[str] = ["collectible_id"]

    ID = 0xb8ea86a9
    QUALNAME = "types.InputPeerColorCollectible"

    def __init__(self, *, collectible_id: int) -> None:
        self.collectible_id = collectible_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerColorCollectible":
        # No flags
        
        collectible_id = Long.read(b)
        
        return InputPeerColorCollectible(collectible_id=collectible_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.collectible_id))
        
        return b.getvalue()
