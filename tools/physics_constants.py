class PhysicsConstants:
    CONSTANTS = {
        "speed_of_light": 299792458,  # m/s
        "gravitational_constant": 6.67430e-11,  # m³/kg/s²
        "planck_constant": 6.62607015e-34,  # J⋅s
        "electron_mass": 9.1093837015e-31,  # kg
        "proton_mass": 1.67262192369e-27,  # kg
        "neutron_mass": 1.67492749804e-27,  # kg
        "avogadro_number": 6.02214076e23,  # mol⁻¹
        "boltzmann_constant": 1.380649e-23,  # J/K
        "gas_constant": 8.31446261815324,  # J/mol/K
        "elementary_charge": 1.602176634e-19,  # C
    }
    
    @classmethod
    def get_constant(cls, name: str) -> float:
        """Get a physics constant by name."""
        name = name.lower().replace(" ", "_")
        if name not in cls.CONSTANTS:
            raise ValueError(f"Constant '{name}' not found")
        return cls.CONSTANTS[name]
    
    @classmethod
    def list_constants(cls) -> list[str]:
        """List all available constants."""
        return list(cls.CONSTANTS.keys())
    
    @classmethod
    def get_constant_with_unit(cls, name: str) -> tuple[float, str]:
        """Get a physics constant with its unit."""
        units = {
            "speed_of_light": "m/s",
            "gravitational_constant": "m³/kg/s²",
            "planck_constant": "J⋅s",
            "electron_mass": "kg",
            "proton_mass": "kg",
            "neutron_mass": "kg",
            "avogadro_number": "mol⁻¹",
            "boltzmann_constant": "J/K",
            "gas_constant": "J/mol/K",
            "elementary_charge": "C",
        }
        value = cls.get_constant(name)
        return value, units[name] 