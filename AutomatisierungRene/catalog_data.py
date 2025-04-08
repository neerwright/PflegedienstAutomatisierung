from dataclasses import dataclass

@dataclass
class Catalog:
    """Class for keeping track of Catalog data"""
    catalog_wage : int = 0
    dates : str = ["1.1.2024 - 02.01.2024", "11.10.2024 - 12.11.2024"] 
    hours : str = ["220,05", "218,7"] 

    
    