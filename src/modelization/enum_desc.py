# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.src.modelization.io_manager.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  Describes an enumeration in the code.

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

from src import DocFileCategory

# ---------------------------------------------------------------------------

class EnumDesc:
    
    def __init__(self, name: str, summary: list[str], items: dict[str, object] = None) -> None:
        """
        SUMMARY
        -------
            This public method is the constructor of the EnumDesc method.

        PARAMETERS
        ----------
            - name (str): The name of the enum
            - summary (list[str]): The description (@brief) of the enum
            - items (dict[str, object]): Optional parameter, the items of the enum
        """
        if values is None:
            values = list()

        self.__name = name
        self.__summary = summary
        self.__items = items
    
    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_name(self) -> str:
        """
        SUMMARY
        -------
            This public method is the getter of the '__name' attribute.
            It returns the name of the enumeration.

        RETURNS
        -------
            str: Enum name
        """
        return self.__name
    
    # ---------------------------------------------------------------------------

    def get_summary(self) -> list[str]:
        """
        SUMMARY
        -------
            This public method is the getter of the '__summary' attribute.
            It returns the description of the enumeration.

        RETURNS
        -------
            list[str]: Enum description
        """
        return self.__summary.copy()

    # ---------------------------------------------------------------------------

    def get_items(self) -> dict[str, object]:
        """
        SUMMARY
        -------
            This public method is the getter of the '__items' attribute.
            It returns all items of the enumeration in dictionary format.

        Returns:
            dict[str, object]: key=ITEM, value=ITEM_VALUE
        """
        return self.__items.copy()

    # ---------------------------------------------------------------------------

    def get_item_value(self, key: str) -> object:
        """
        SUMMARY
        -------
            This public method return the value of a given item of the enum.

        PARAMETERS
        ----------
            - key (str): The item of the enum

        RETURNS
        -------
            object: The value of the given item
        """
        return self.__items.get(key)

    # ---------------------------------------------------------------------------
    # SETTERS
    # ---------------------------------------------------------------------------

    def add_item(self, key: str, value: object) -> None:
        """
        SUMMARY
        -------
            This public method is the setter of the '__items' attribute.
            It append a new item in the instance, re-set the new value if the key already exists.

        PARAMETERS
        ----------
            - key (str): The name of the item
            - value (object): The value of the item
        """
        self.__items[key] = value

    # ---------------------------------------------------------------------------
    # PUBLIC METHODS
    # ---------------------------------------------------------------------------

    def to_markdown(self, output: str, file_container: str) -> list[str]:
        """
        SUMMARY
        -------
            This public method generates markdown to describe this enum.

        RETURNS
        -------
            list[str]: The lines of the markdown generated.
        """
        lines: list[str] = list()

        lines.append(f"# (enum) {self.__name}")
        lines.extend(self.__summary)
        lines.append("")
        lines.append(f"## Items")
        lines.append("")

        lines.append("| ITEM | VALUE |")
        lines.append("|------|-------|")

        for key, value in self.__items:
            lines.append(f"| {key} | {value} |")

        lines.append("")
        lines.append("## Location")
        lines.append("")

        doc_file_path = os.path.join(output, DocFileCategory.FILE.value, file_container + ".md")
        lines.append(f"[{file_container}]({doc_file_path})")
        lines.append("")

        return lines
