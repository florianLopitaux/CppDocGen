# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.src.modelization.tag.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  Represents a tag (@something value) in the docstring of the code.

-------------------------------------------------------------------------

Copyright (C) 2023 Florian Lopitaux

Use of this software is governed by the GNU Public License, version 3.

CppDocGen is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CppDocGen is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CppDocGen. If not, see <http://www.gnu.org/licenses/>.

This banner notice must not be removed.

-------------------------------------------------------------------------

"""

from enum import Enum
from typing import Self

# ---------------------------------------------------------------------------

class TagKeys(Enum):
    FILE = "file",
    NAMESPACE = "namespace",
    CLASS = "class",
    ENUMERATION = "enum",
    METHOD = "method",
    FUNCTION = "func",
    AUTHOR = "author",
    VERSION = "version",
    BRIEF = "brief",
    PARAMETER = "param",
    EXCEPTION = "throw",
    RETURN = "return"

    @classmethod
    def from_string(self, key: str) -> Self:
        for current_key in TagKeys:
            if key == current_key.value:
                return key
        
        return None


# ---------------------------------------------------------------------------


class Tag:

    def __init__(self, key: TagKeys, value: str = None) -> None:
        self.__key: TagKeys = key
        self.__value: str = value

    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_key(self) -> TagKeys:
        return self.__key
