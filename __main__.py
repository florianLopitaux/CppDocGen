# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.__main__.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  Entrypoint of the CppDocGen program.

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

import os
import argparse

# ---------------------------------------------------------------------------


def set_program_options(args_parser: argparse.ArgumentParser) -> None:
    """
    SUMMARY
    -------
        This function set all arguments and options in the argument parser to use the script in CLI.

    PARAMETERS
    ----------
        - args_parser (argparse.ArgumentParser): The argument parser of the script
    """
    args_parser.add_argument("input", type=str,
                             help="The root directory path that contains the c++ codes")
    args_parser.add_argument("-o", "--output", type=str, default=os.path.dirname(__file__),
                             help="The output directory path that will contain all generated documentation")

# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # configure program arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Generate a markdown documentation of C++ code")
    set_program_options(parser)

    args: argparse.Namespace = parser.parse_args()
