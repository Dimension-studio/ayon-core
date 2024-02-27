
"""
Trait definitions in the 'identity' namespace.

Traits that aid the identification of an entity.
"""

# WARNING: This file is auto-generated by openassetio-traitgen, do not edit.

from typing import Union

from openassetio.trait import TraitsData


class DisplayNameTrait:
    """
    Names that can be presented to a user in order to identify and/or
    disambiguate the entity. These strings are potentially unstable and
    should not be used as a UUID or other persistent anchor.
    Usage: entity
    """
    kId = "openassetio-mediacreation:identity.DisplayName"

    def __init__(self, traitsData):
        """
        Construct this trait view, wrapping the given data.

        @param traitsData @fqref{TraitsData}} "TraitsData" The target
        data that holds/will hold the traits properties.
        """
        self.__data = traitsData

    def isImbued(self):
        """
        Checks whether the data this trait has been applied to
        actually has this trait.
        @return `True` if the underlying data has this trait, `False`
        otherwise.
        """
        return self.isImbuedTo(self.__data)

    @classmethod
    def isImbuedTo(cls, traitsData):
        """
        Checks whether the given data actually has this trait.
        @param traitsData: Data to check for trait.
        @return `True` if the underlying data has this trait, `False`
        otherwise.
        """
        return traitsData.hasTrait(cls.kId)

    def imbue(self):
        """
        Adds this trait to the held data.

        If the data already has this trait, it is a no-op.
        """
        self.__data.addTrait(self.kId)

    @classmethod
    def imbueTo(cls, traitsData):
        """
        Adds this trait to the provided data.

        If the data already has this trait, it is a no-op.
        """
        traitsData.addTrait(cls.kId)

    
    def setName(self, name: str):
        """
        Sets the name property.

        The humanized name of entity itself, not including any hierarchy
        or classification.

        For example: - `"Cuttlefish v1"` - for a version of an asset -
        `"seq003"` - for a sequence in a hierarchy
        """
        if not isinstance(name, str):
            raise TypeError("name must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "name", name)

    def getName(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the name property or the supplied default.

        The humanized name of entity itself, not including any hierarchy
        or classification.

        For example: - `"Cuttlefish v1"` - for a version of an asset -
        `"seq003"` - for a sequence in a hierarchy
        """
        value = self.__data.getTraitProperty(self.kId, "name")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    def setQualifiedName(self, qualifiedName: str):
        """
        Sets the qualifiedName property.

        An unambiguous, humanized name for the entity.

        The display name may want to consider the host, and any other
        relevant Context information to form a display name for an
        entity that can uniquely identify the entity in that context.

        For example: - `"dive / build / cuttlefish / model / v1"` for a
        version
            of an asset in an 'open recent' menu.
        - `"Sequence 003 [ Dive / Episode 1 ]"` for a sequence in
           a hierarchy as a window title.
        """
        if not isinstance(qualifiedName, str):
            raise TypeError("qualifiedName must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "qualifiedName", qualifiedName)

    def getQualifiedName(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the qualifiedName property or the supplied default.

        An unambiguous, humanized name for the entity.

        The display name may want to consider the host, and any other
        relevant Context information to form a display name for an
        entity that can uniquely identify the entity in that context.

        For example: - `"dive / build / cuttlefish / model / v1"` for a
        version
            of an asset in an 'open recent' menu.
        - `"Sequence 003 [ Dive / Episode 1 ]"` for a sequence in
           a hierarchy as a window title.
        """
        value = self.__data.getTraitProperty(self.kId, "qualifiedName")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    
