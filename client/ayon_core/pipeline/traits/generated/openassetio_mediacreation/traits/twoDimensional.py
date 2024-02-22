
"""
Trait definitions in the 'twoDimensional' namespace.

Traits that are concerned with describing two-dimensional data, more
colloquially known as 'images'.
"""

# WARNING: This file is auto-generated by openassetio-traitgen, do not edit.

from typing import Union

from openassetio.trait import TraitsData


class DeepTrait:
    """
    The entity data contains multiple depth samples for each data point
    in the two dimensional width/height domain.
    Usage: entity
    """
    kId = "openassetio-mediacreation:twoDimensional.Deep"

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

    


class ImageTrait:
    """
    A family trait that should be composed with more specific traits for
    any entity that holds two-dimensional data.
    Usage: entity
    """
    kId = "openassetio-mediacreation:twoDimensional.Image"

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

    


class PixelBasedTrait:
    """
    Entity data is encoded in a pixel grid of two dimensions. Also known
    as 'raster' data.

    Note: Properties (or most likely traits) to describe overscan and/or
    other cases where the data window differs, need to be added once we
    have a more concrete definition of required workflows.
    Usage: entity
    """
    kId = "openassetio-mediacreation:twoDimensional.PixelBased"

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

    
    def setDisplayWindowHeight(self, displayWindowHeight: int):
        """
        Sets the displayWindowHeight property.

        The number of pixels in the height dimension before pixel aspect
        ratio is taken into account. If the data contains additional
        hidden pixels (overscan) then this should not be included in
        this value.
        """
        if not isinstance(displayWindowHeight, int):
            raise TypeError("displayWindowHeight must be a 'int'.")
        self.__data.setTraitProperty(self.kId, "displayWindowHeight", displayWindowHeight)

    def getDisplayWindowHeight(self, defaultValue: int=None) -> Union[int, None]:
        """
        Gets the value of the displayWindowHeight property or the supplied default.

        The number of pixels in the height dimension before pixel aspect
        ratio is taken into account. If the data contains additional
        hidden pixels (overscan) then this should not be included in
        this value.
        """
        value = self.__data.getTraitProperty(self.kId, "displayWindowHeight")
        if value is None:
            return defaultValue

        if not isinstance(value, int):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'int'.")
            return defaultValue
        return value
        
    def setDisplayWindowWidth(self, displayWindowWidth: int):
        """
        Sets the displayWindowWidth property.

        The number of pixels in the width dimension before pixel aspect
        ratio is taken into account. If the data contains additional
        hidden pixels (overscan) then this should not be included in
        this value.
        """
        if not isinstance(displayWindowWidth, int):
            raise TypeError("displayWindowWidth must be a 'int'.")
        self.__data.setTraitProperty(self.kId, "displayWindowWidth", displayWindowWidth)

    def getDisplayWindowWidth(self, defaultValue: int=None) -> Union[int, None]:
        """
        Gets the value of the displayWindowWidth property or the supplied default.

        The number of pixels in the width dimension before pixel aspect
        ratio is taken into account. If the data contains additional
        hidden pixels (overscan) then this should not be included in
        this value.
        """
        value = self.__data.getTraitProperty(self.kId, "displayWindowWidth")
        if value is None:
            return defaultValue

        if not isinstance(value, int):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'int'.")
            return defaultValue
        return value
        
    def setPixelAspectRatio(self, pixelAspectRatio: float):
        """
        Sets the pixelAspectRatio property.

        The aspect ratio of each pixel expressed as width divided by
        height. The value represents how much the width of the pixel
        should be stretched for display.
        """
        if not isinstance(pixelAspectRatio, float):
            raise TypeError("pixelAspectRatio must be a 'float'.")
        self.__data.setTraitProperty(self.kId, "pixelAspectRatio", pixelAspectRatio)

    def getPixelAspectRatio(self, defaultValue: float=None) -> Union[float, None]:
        """
        Gets the value of the pixelAspectRatio property or the supplied default.

        The aspect ratio of each pixel expressed as width divided by
        height. The value represents how much the width of the pixel
        should be stretched for display.
        """
        value = self.__data.getTraitProperty(self.kId, "pixelAspectRatio")
        if value is None:
            return defaultValue

        if not isinstance(value, float):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'float'.")
            return defaultValue
        return value
        
    


class PlanarTrait:
    """
    The entity data contains a single sample for each data point in the
    two dimensional width/height domain, such that the resulting image
    lies on a plane.
    """
    kId = "openassetio-mediacreation:twoDimensional.Planar"

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

    

