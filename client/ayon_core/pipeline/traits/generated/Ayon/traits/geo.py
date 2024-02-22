
"""
Trait definitions in the 'geo' namespace.

Traits related to geometry.
"""

# WARNING: This file is auto-generated by openassetio-traitgen, do not edit.

from typing import Union

from openassetio.trait import TraitsData


class ArchiveTrait:
    """
    A trait indicating an archive.
    Usage: entity
    """
    kId = "Ayon:geo.Archive"

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

    
    def setRenderer(self, renderer: str):
        """
        Sets the renderer property.

        Renderer of the archive.
        """
        if not isinstance(renderer, str):
            raise TypeError("renderer must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "renderer", renderer)

    def getRenderer(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the renderer property or the supplied default.

        Renderer of the archive.
        """
        value = self.__data.getTraitProperty(self.kId, "renderer")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    


class CameraTrait:
    """
    A trait indicating a camera.
    Usage: entity
    """
    kId = "Ayon:geo.Camera"

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

    


class LookTrait:
    """
    A trait indicating a look.
    Usage: entity
    """
    kId = "Ayon:geo.Look"

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

    


class ModelTrait:
    """
    A trait indicating a model.
    Usage: entity
    """
    kId = "Ayon:geo.Model"

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

    
    def setBoundingBox(self, boundingBox: str):
        """
        Sets the boundingBox property.

        Bounding box of the model.
        """
        if not isinstance(boundingBox, str):
            raise TypeError("boundingBox must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "boundingBox", boundingBox)

    def getBoundingBox(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the boundingBox property or the supplied default.

        Bounding box of the model.
        """
        value = self.__data.getTraitProperty(self.kId, "boundingBox")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    


class PointCacheTrait:
    """
    A trait indicating a pointcache.
    Usage: entity
    """
    kId = "Ayon:geo.PointCache"

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

    


class ProxyTrait:
    """
    A trait indicating a proxy.
    Usage: entity
    """
    kId = "Ayon:geo.Proxy"

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

    


class RigTrait:
    """
    A trait indicating a rig.
    Usage: entity
    """
    kId = "Ayon:geo.Rig"

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

    


class SpatialContentTrait:
    """
    A trait indicating a spatial content.
    Usage: entity
    """
    kId = "Ayon:geo.SpatialContent"

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

    
    def setBoundingBox(self, boundingBox: str):
        """
        Sets the boundingBox property.

        Bounding box of the spatial content.
        """
        if not isinstance(boundingBox, str):
            raise TypeError("boundingBox must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "boundingBox", boundingBox)

    def getBoundingBox(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the boundingBox property or the supplied default.

        Bounding box of the spatial content.
        """
        value = self.__data.getTraitProperty(self.kId, "boundingBox")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    def setFrontAxis(self, frontAxis: str):
        """
        Sets the frontAxis property.

        Front axis of the spatial content.
        """
        if not isinstance(frontAxis, str):
            raise TypeError("frontAxis must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "frontAxis", frontAxis)

    def getFrontAxis(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the frontAxis property or the supplied default.

        Front axis of the spatial content.
        """
        value = self.__data.getTraitProperty(self.kId, "frontAxis")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    def setUnits(self, units: str):
        """
        Sets the units property.

        Units of the spatial content.
        """
        if not isinstance(units, str):
            raise TypeError("units must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "units", units)

    def getUnits(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the units property or the supplied default.

        Units of the spatial content.
        """
        value = self.__data.getTraitProperty(self.kId, "units")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    def setUpAxis(self, upAxis: str):
        """
        Sets the upAxis property.

        Up axis of the spatial content.
        """
        if not isinstance(upAxis, str):
            raise TypeError("upAxis must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "upAxis", upAxis)

    def getUpAxis(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the upAxis property or the supplied default.

        Up axis of the spatial content.
        """
        value = self.__data.getTraitProperty(self.kId, "upAxis")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    


class VolumeTrait:
    """
    A trait indicating a volume.
    Usage: entity
    """
    kId = "Ayon:geo.Volume"

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

    
    def setBoundingBox(self, boundingBox: str):
        """
        Sets the boundingBox property.

        Bounding box of the volume.
        """
        if not isinstance(boundingBox, str):
            raise TypeError("boundingBox must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "boundingBox", boundingBox)

    def getBoundingBox(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the boundingBox property or the supplied default.

        Bounding box of the volume.
        """
        value = self.__data.getTraitProperty(self.kId, "boundingBox")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    def setGrids(self, grids: str):
        """
        Sets the grids property.

        Grids of the volume.
        """
        if not isinstance(grids, str):
            raise TypeError("grids must be a 'str'.")
        self.__data.setTraitProperty(self.kId, "grids", grids)

    def getGrids(self, defaultValue: str=None) -> Union[str, None]:
        """
        Gets the value of the grids property or the supplied default.

        Grids of the volume.
        """
        value = self.__data.getTraitProperty(self.kId, "grids")
        if value is None:
            return defaultValue

        if not isinstance(value, str):
            if defaultValue is None:
                raise TypeError(f"Invalid stored value type: '{type(value).__name__}' should be 'str'.")
            return defaultValue
        return value
        
    

