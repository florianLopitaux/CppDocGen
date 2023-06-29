# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.src.io_manager.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  File which manages the I/O interaction with the program.

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
from enum import Enum

# ---------------------------------------------------------------------------

# list which contains all extensions possibles for a c++ file.
CPP_EXTENSIONS: list[str] = [".h", ".hpp", ".cpp", ".cxx", ".cc", ".c"]

# ---------------------------------------------------------------------------


class DocFileCategory(Enum):
    """
    SUMMARY
    -------
        This class is an enumeration of all documentation files categories.
        The value of each item is the name of the sub directory that contains this type of doc files.
    """
    FILE = "files"
    CLASS = "classes"
    FUNCTION = "functions"
    NAMESPACE = "namespaces"


# ---------------------------------------------------------------------------


class IOManager:
    """
    SUMMARY
    -------
        This class manages all I/O interactions with the program.
    """

    def __init__(self, input_dir_root: str, output_dir_root: str) -> None:
        if not os.path.isdir(input_dir_root):
            raise FileNotFoundError(f"The directory {input_dir_root} doesn't exist !")

        self.__files: list[str] = list()
        self.__search_all_files(input_dir_root)

        self.__output_dir: str = output_dir_root
        self.__initialize_doc_directory()

    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_files(self) -> list[str]:
        """
        SUMMARY
        -------
            This public method is the getter of the '__files' attribute.
            It returns the list of all c++ files in the input root directory to process.

        RETURNS
        -------
            list[str]: All c++ files path
        """
        return self.__files

    # ---------------------------------------------------------------------------
    # PUBLIC METHODS
    # ---------------------------------------------------------------------------

    def create_file(self, name: str, content: list[str], category: DocFileCategory = None) -> None:
        """
        SUMMARY
        -------
            This public method creates a file in the documentation output directory.

        PARAMETERS
        ----------
            - name (str): The name of the file to create
            - content (str): The markdown content of the file
            - category (DocFileCategory): Optional parameter, the documentation category of the file
                       By default, The file is create in the root.

        RAISES
        ------
            - FileExistsError: Raise if the file to create already exists.
        """
        if category is None:
            complete_file_path = os.path.join(self.__output_dir, name + ".md")
        else:
            complete_file_path = os.path.join(self.__output_dir, category.value, name + ".md")

        if os.path.exists(complete_file_path):
            raise FileExistsError(f"The file '{complete_file_path}' already exists !")
        
        with open(complete_file_path, 'w') as file:
            file.writelines(content)

    # ---------------------------------------------------------------------------
    # PRIVATE METHODS
    # ---------------------------------------------------------------------------

    def __search_all_files(self, dir_root: str) -> None:
        """
        SUMMARY
        -------
            This private methods finds all c++ files in the given directory.

        PARAMETERS
        ----------
            - dir_root (str): The path of the directory where to look
        """
        for root, _, files in os.walk(dir_root):
            for file in files:
                _, file_extension: str = os.path.splitext(file)

                if file_extension.lower() in CPP_EXTENSIONS:
                    self.__files.append(os.path.join(root, files))

    # ---------------------------------------------------------------------------

    def __initialize_doc_directory(self) -> None:
        """
        SUMMARY
        -------
            This private method creates the output directory and all sub directories for each file category.
        """
        os.mkdir(self.__output_dir)

        for category in DocFileCategory:
            os.mkdir(category.value)
