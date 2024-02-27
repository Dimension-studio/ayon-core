
"""
Trait definitions in the 'relationship' namespace.

Traits specific to qualities of a relationship.
"""

# WARNING: This file is auto-generated by openassetio-traitgen, do not edit.

from typing import Union

from openassetio.trait import TraitsData


class SingularTrait:
    """
    The relationship should return at most one reference for each input.
    Unless otherwise qualified, relationships are considered one-to-
    many.
    Usage: relationship
    """
    kId = "openassetio-mediacreation:relationship.Singular"

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

    


class UnboundedTrait:
    """
    The relationship may return large numbers of results for each input,
    and so must be used with the paged API methods, such as
    Manager.getWithRelationshipPaged.
    Usage: relationship
    """
    kId = "openassetio-mediacreation:relationship.Unbounded"

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

    
