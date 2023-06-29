# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.src.modelization.__init__.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  Init file of the 'modelization' folder to simplify the imports.

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

# check python version to use the program
import sys

if sys.version_info < (3, 11):
    sys.exit("Python version inferior to 3.11 is unsurpotted for the program.")

# ---------------------------------------------------------------------------

from .enum_desc import EnumDesc


__all__ = {
    "EnumDesc"
}
