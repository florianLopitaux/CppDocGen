# -*- coding: UTF-8 -*-
"""
:filename: CppDocGen.src.modelization.tags.py
:author:   Florian Lopitaux
:version:  0.1
:summary:  Represents a tag (@key {values}) in the docstrings of the code.

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
from copy import copy

from src.modelization.tags import TagKeys

# ---------------------------------------------------------------------------


class TagKeys(Enum):
    """
    SUMMARY
    -------
        This class is an enumeration that list all docstring keys supported.
    """
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
        """
        SUMMARY
        -------
            This public method returns the item of the enumeration corresponding with the given key.

        PARAMETERS
        ----------
            - key (str): The key in the docstring

        RETURNS
        -------
            Self: The item of the enumeration corresponding.
        """
        for current_key in TagKeys:
            if key == current_key.value:
                return key
        
        return None


# ---------------------------------------------------------------------------


class Tag:
    """
    SUMMARY
    -------
        This class represents a simple tag in the docstring (@key {value}) 
    """

    def __init__(self, key: TagKeys, value: str | list[str] = None) -> None:
        """
        SUMMARY
        -------
            This public method is the constructor of the 'Tag' class.

        PARAMETERS
        ----------
            - key (TagKeys): The key of the tag
            - value (str | list[str]): Optional parameter, the value of the tag (one or multiple lines)
        """
        if value is None:
            value = list()

        self._key: TagKeys = key
        self._value: str | list[str] = value

    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_key(self) -> TagKeys:
        """
        SUMMARY
        -------
            This public method is the getter of the '_key' attribute.
            Returns the key of the tag.

        RETURNS
        -------
            TagKeys: The tag key
        """
        return self._key
    
    # ---------------------------------------------------------------------------

    def get_value(self) -> str | list[str]:
        """
        SUMMARY
        -------
            This public method is the getter of the '_value' attribute.
            Returns the value of the tag.

        RETURNS
        -------
            str | list[str]: The tag value (one or multiple lines)
        """
        return self._value

    # ---------------------------------------------------------------------------
    # SETTERS
    # ---------------------------------------------------------------------------

    def set_value(self, value: str | list[str]) -> None:
        """
        SUMMARY
        -------
            This public method is the setter of the '_value' attribute.
            Set or appends (depending if we have one or multiple lines) the given value.

        PARAMETERS
        ----------
            - value (str | list[str]): The value to set or append

        RAISES
        ------
            - ValueError: If the value isn't an instance of 'str' or 'list'
        """
        if isinstance(value, str):
            self._value = value
        elif isinstance(value, list) and isinstance(self._value, list):
            self._value.extend(value)
        else:
            raise ValueError(f"The 'value' parameter must be a 'str' or 'list' instance but not {value}")
        
    # ---------------------------------------------------------------------------
    # OVERLOADS copy
    # ---------------------------------------------------------------------------

    def __copy__(self) -> Self:
        """
        SUMMARY
        -------
            Overloads of copy method.

        RETURNS
        -------
            Self: The object copy of the instance.
        """
        return Tag(self._key, value=self._value)


# ---------------------------------------------------------------------------


class TypedTag(Tag):
    """
    SUMMARY
    -------
        This class represents a tag with a type (for throw and return key).
        TypedTag pattern: @key {type} {value}
    """

    def __init__(self, key: TagKeys, value: str | list[str] = None,
                 type: str = None) -> None:
        """
        SUMMARY
        -------
            This public method is the constructor of the 'TypedTag' class.
        
        PARAMETERS
        ----------
            - key (TagKeys): The key of the tag
            - value (str | list[str]): Optional parameter, the value of the tag (one or multiple lines)
            - type (str): Optional parameter, the type of the tag
        """

        super().__init__(key, value)
        self._type: str = type
    
    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_type(self) -> str:
        """
        SUMMARY
        -------
            This public method is the getter of the '_type' attribute.
            Returns the type of the tag.

        RETURNS
        -------
            str: The tag type
        """
        return self._type
    
    # ---------------------------------------------------------------------------
    # SETTERS
    # ---------------------------------------------------------------------------

    def set_type(self, type: str) -> None:
        """
        SUMMARY
        -------
            This public method is the setter of the '_type' attribute.
            Set the type of the tag.
        
        PARAMETERS
        ----------
            - type (str): The tag type to set
        """
        self._type = type

    # ---------------------------------------------------------------------------
    # OVERLOADS copy
    # ---------------------------------------------------------------------------

    def __copy__(self) -> Self:
        """
        SUMMARY
        -------
            Overloads of copy method.

        RETURNS
        -------
            Self: The object copy of the instance.
        """
        return TypedTag(self._key, type=self._type, value=self._value)


# ---------------------------------------------------------------------------


class ParameterTag(TypedTag):
    """
    SUMMARY
    -------
        This class represents a parameter tag in function or method (only for parameter key).
        ParameterTag pattern: @key {name} {type} {hints} {value}
    """

    def __init__(self, key: TagKeys, value: str | list[str] = None,
                 type: str = None,
                 name: str = None, hints: list[str] = None) -> None:
        """
        SUMMARY
        -------
            This public method is the constructor of the 'ParameterTag' class.

        PARAMETERS
        ----------
            - key (TagKeys): The key of the tag
            - value (str | list[str]): Optional parameter, the value of the tag (one or multiple lines)
            - type (str): Optional parameter, the type of the tag
            - name (str): Optional parameter, the name of the tag
            - hints (list[str]): Optional parameter, the hints of the tag (in, out, in/out, optional...)
        """

        super().__init__(key, type, value)

        if hints is None:
            hints = list()

        self._name: str = name
        self._hints: list[str] = hints

    # ---------------------------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------------------------

    def get_name(self) -> str:
        """
        SUMMARY
        -------
            This public methods is the getter of the '_name' attribute.
            Returns the name of the parameter tag.
        
        RETURNS
        -------
            str: The parameter tag name
        """
        return self._name
    
    # ---------------------------------------------------------------------------

    def get_hints(self) -> list[str]:
        """
        SUMMARY
        -------
            This public methods is the getter of the '_hints' attribute.
            Returns the hints of the parameter tag.

        RETURNS
        -------
            list[str]: The parameter tag hints
        """
        return self._hints.copy()
    
    # ---------------------------------------------------------------------------
    # SETTERS
    # ---------------------------------------------------------------------------

    def set_name(self, name: str) -> None:
        """
        SUMMARY
        -------
            This public methods is the setter of the '_name' attribute.
            Set the name of the parameter tag.

        PARMETERS
        ---------
            - name (str): The parameter tag name to set
        """
        self._name = name

    # ---------------------------------------------------------------------------

    def add_hints(self, hints: list[str]) -> None:
        """
        SUMMARY
        -------
            This public methods is the setter of the '_hints' attribute.
            Adds new hints of the parameter tag.

        PARMETERS
        ---------
            - hints (list[str]): The parameter tag hints to add
        """
        self._hints.extend(hints)

    # ---------------------------------------------------------------------------
    # OVERLOADS copy
    # ---------------------------------------------------------------------------

    def __copy__(self):
        """
        SUMMARY
        -------
            Overloads of copy method.

        RETURNS
        -------
            Self: The object copy of the instance.
        """
        return ParameterTag(self._key, value=self._value, type=self._type, name=self._name, hints=self._hints)
