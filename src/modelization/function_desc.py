# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.src.modelization.function_desc.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  Describes an enumeration of the code.

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
import copy

from src import DocFileCategory
from .tags import TypedTag, ParameterTag

# ---------------------------------------------------------------------------


class FunctionDesc:
    """
    SUMMARY
    -------
        This class is described a function of the code.
    """

    def __init__(self, name: str, declare_code_line: str,
                 summary: list[str] = None, return_tag: TypedTag = None,
                 parameters: list[ParameterTag] = None, exceptions: list[TypedTag] = None) -> None:

        if summary is None:
            summary = list()

        if parameters is None:
            parameters = list()

        if exceptions is None:
            exceptions = list()

        self.__name: str = name
        self.__code_line: str = declare_code_line

        self.__summary: list[str] = summary
        self.__parameters: list[ParameterTag] = parameters
        self.__exceptions: list[TypedTag] = exceptions
        self.__return: TypedTag | None = return_tag

    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_name(self) -> str:
        return self.__name
    
    # ---------------------------------------------------------------------------

    def get_summary(self) -> list[str]:
        return self.__summary

    # ---------------------------------------------------------------------------

    def get_parameters(self) -> list[ParameterTag]:
        return copy.deepcopy(self.__parameters)

    # ---------------------------------------------------------------------------

    def get_parameter(self, name: str) -> ParameterTag | None:
        for param in self.__parameters:
            if param.get_name() == name:
                return copy.copy(param)
        
        return None
    
    # ---------------------------------------------------------------------------

    def get_throws(self) -> list[TypedTag]:
        return copy.deepcopy(self.__exceptions)

    # ---------------------------------------------------------------------------

    def get_throw(self, exception: str) -> TypedTag | None:
        for exception in self.__exceptions:
            if exception.get_type() == exception:
                return copy.copy(exception)

        return None

    # ---------------------------------------------------------------------------

    def get_return_tag(self) -> TypedTag | None:
        return copy.copy(self.__return)

    # ---------------------------------------------------------------------------
    # SETTERS
    # ---------------------------------------------------------------------------

    def set_summary(self, summary: list[str]) -> None:
        self.__summary = summary

    # ---------------------------------------------------------------------------

    def add_to_summary(self, lines: list[str]) -> None:
        self.__summary.extend(lines)

    # ---------------------------------------------------------------------------

    def add_parameters(self, parameters: list[ParameterTag]) -> None:
        if any(not isinstance(current, ParameterTag) for current in parameters):
            raise ValueError(f"The 'parameters' parameter must be contain only 'ParameterTag' instances !\Variable : {parameters}")

        self.__parameters.extend(parameters)

    # ---------------------------------------------------------------------------

    def add_exceptions(self, exceptions: list[TypedTag]) -> None:
        if any(not isinstance(current, TypedTag) for current in exceptions):
            raise ValueError(f"The 'exceptions' parameter must be contain only 'TypedTag' instances !\Variable : {exceptions}")

        self.__exceptions.extend(exceptions)

    # ---------------------------------------------------------------------------

    def set_return_tag(self, return_tag: TypedTag) -> None:
        if isinstance(return_tag, TypedTag):
            self.__return = return_tag
        else:
            raise ValueError(f"The 'return_tag' parameter must be a 'TypedTag' instance and not '{type(return_tag)}' !")

    # ---------------------------------------------------------------------------
    # PUBLIC METHODS
    # ---------------------------------------------------------------------------
    
    def generate_markdown(self, output: str, file_container: str, class_container: str = None) -> list[str]:
        """
        SUMMARY
        -------
            This public method generates markdown to describe this enum.

        PARAMETERS
        ----------
            - output (str): The path of the output documentation directory
            - file_container (str) The name of the file that contains this enum 

        RETURNS
        -------
            list[str]: The lines of the markdown generated
        """
        lines: list[str] = list()
        lines.append(f"# {self.__name} - (function)")
        lines.append("")

        lines.append("```cpp")
        lines.append(self.__code_line)
        lines.append("```")
        lines.append("")

        for line in self.__summary:
            lines.append(f"> {line}")
        lines.append("")

        lines.append(f"## Parameters")
        lines.append("")
        lines.append("| NAME | TYPE | HINTS | DESCRIPTION |")
        lines.append("|------|------|-------|-------------|")

        for param in self.__parameters:
            lines.append(f"| {param.get_name()} | {param.get_type()} | {param.get_hints()} | {param.get_value()} |")

        lines.append("")
        lines.append("## Raises")
        lines.append("")
        lines.append("| EXCEPTION | DESCRIPTION |")
        lines.append("|-----------|-------------|")

        for exception in self.__raises:
            lines.append(f"| {exception.get_type()} | {exception.get_value()} |")

        lines.append("")
        lines.append("## Returns")
        lines.append("")

        lines.append("| TYPE | DESCRIPTION |")
        lines.append("|------|-------------|")
        lines.append(f"| {self.__return.get_type()} | {self.__return.get_value()} |")
        lines.append("")

        lines.append("## Location")
        doc_file_path = os.path.join(output, DocFileCategory.FILE.value, file_container + ".md")
        lines.append(f"File: [{file_container}]({doc_file_path})")

        if class_container is None:
            lines.append("Class: No class associated")
        else:
            doc_class_path = os.path.join(output, DocFileCategory.CLASS.value, class_container + ".md")
            lines.append(f"Class: [{class_container}]({doc_class_path})")

        lines.append("")
        return lines
