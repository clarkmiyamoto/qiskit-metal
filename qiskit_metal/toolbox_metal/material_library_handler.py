from pandas import pd

material_library_path = 'material_library.csv'
"""Relative path to material library"""

material_df = pd.read_csv(material_library_path)
"""DataFrame of Materials"""

supported_materials = list(material_df['name'])
"""Supported materials"""

def material_to_dict(material_name: str) -> dict:
    """
    Find material characteristics from material_library.csv

    Args:
        material_name (str): Find material by 'name' column in material_library.csv.

    Returns:
        material_characteristics (dict): Characteristics of referenced material.
    """
    material_name = material_name.lower()
    if material_name not in supported_materials:
        raise ValueError(f'material_name is currently not supported in qiskit_metal.toolbox_metal.material_library.csv. Use one of the following {supported_materials}')
    
    target_material = material_df[material_df['name'] == material_name]
    material_characteristics = target_material.to_dict()
    
    return material_characteristics
