import pandas as pd
from qiskit_metal.toolbox_metal import material_library_handler

class PalaceMaterial:
    """
    Class is used for managing materials associated w/ Palace.
    """

    def __init__(self, Name: str, Attributes: list[int], Permeability: float, 
                 Permittivity: float, LossTan: float, Conductivity: float, 
                 LondonDepth: float, MaterialAxes: list):
        """Create a custom material"""
        self.Name = Name
        self.Attributes = Attributes
        self.Permeability = Permeability
        self.Permittivity = Permittivity
        self.LossTan = LossTan
        self.Conductivity = Conductivity
        self.LondonDepth = LondonDepth
        self.MaterialAxes = MaterialAxes
    
    def __str__(self):
        return f"PalaceMaterial: {self.name} assigned to components {self.attributes}"

    def dict_for_json(self) -> dict:
        package = {
            "Attributes": self.Attributes,
            "Permeability": self.Permeability,
            "Permittivity": self.Permittivity,
            "LossTan": self.LossTan,
            "Conductivity": self.Conductivity,
            "LondonDepth": self.LondonDepth,
            "MaterialAxes": self.MaterialAxes,
        }
        return package

    @staticmethod
    def find_material_characteristics(self, material_name):
        """
        Find charactersitics of a material

        Args:
            material_name (str): Name of material for look up
        
        Returns:
            material (PalaceMaterial)
        """
        material_character = material_library_handler.material_to_dict(material_name=material_name)
        material = PalaceMaterial(Name=str(material_character['name']),
                                Attributes=list(),
                                Permeability=float(material_character['permeability']),
                                Permittivity=float(material_character['permittivity']),
                                LossTan=float(material_character['loss_tan']),
                                Conductivity=float(material_character['conductivity']),
                                LondonDepth=float(material_character['london_depth']),
                                MaterialAxes=material_character['material_axes'])
        return material