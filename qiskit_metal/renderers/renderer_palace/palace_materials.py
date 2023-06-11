class PalaceMaterial:
    def __init__(self, name: str, attributes: List(int), permeability: float, 
                 permittivity: float, loss_tan: float, conductivity: float, 
                 london_depth: float, material_axes: list):
        self.name = name
        self.attributes = attributes
        self.permeability = permeability
        self.permittivity = permittivity
        self.loss_tan = loss_tan
        self.conductivity = conductivity
        self.london_depth = london_depth
        self.material_axes = material_axes
    
    def __str__(self):
        return f"PalaceMaterial: {self.name} assigned to components {self.attributes}"

    def dict_for_json(self) -> dict:
        package = {
            "Permeability": self.permeability,
            "Permittivity": self.permittivity,
            "LossTan": self.loss_tan,
            "Conductivity": self.conductivity,
            "LondonDepth": self.london_depth,
            "MaterialAxes": self.material_axes,
        }
        return package
