from abc import ABC, abstractmethod
from decimal import Decimal
from json import load
from pathlib import Path
import bisect


class Unit(ABC):
    """
    Abstract base class representing a unit of measurement.

    Subclasses must implement conversion to and from SI (International System of Units).
    """
    @abstractmethod
    def get_name(self) -> str:
        """
        Returns the full name of the unit.

        Returns:
            str: The name of the unit.
        """
        ...

    @abstractmethod
    def get_abbr(self) -> str:
        """
        Returns the abbreviation of the unit.

        Returns:
            str: The abbreviated form of the unit.
        """
        ...

    @abstractmethod
    def from_si(self, value: Decimal) -> Decimal:
        """
        Converts a value from SI units to this unit.

        Args:
            value (Decimal): The value in SI units.

        Returns:
            Decimal: The value converted to this unit.
        """
        ...

    @abstractmethod
    def to_si(self, value: Decimal) -> Decimal:
        """
        Converts a value from this unit to SI units.

        Args:
            value (Decimal): The value in this unit.

        Returns:
            Decimal: The value converted to SI units.
        """
        ...


class LinearUnit(Unit):
    """
    Represents a linear unit of measurement with an affine transformation
    (i.e., includes both scaling and offset).

    The transformation is defined by:
        y = m * x + c
    where:
        - m is the scaling factor
        - c is the offset
    """
    def __init__(self, name: str, abbr: str, m: Decimal, c: Decimal):
        """
        Initializes the linear unit with a name, abbreviation, scale, and offset.

        Args:
            name (str): The full name of the unit.
            abbr (str): The unit abbreviation.
            m (Decimal): The scaling factor.
            c (Decimal): The offset value.
        """
        self.name = name
        self.abbr = abbr
        self.m = m
        self.c = c

    def get_name(self) -> str:
        """
        Returns the full name of the unit.

        Returns:
            str: The name of the unit.
        """
        return self.name

    def get_abbr(self) -> str:
        """
        Returns the abbreviation of the unit.

        Returns:
            str: The abbreviated form of the unit.
        """
        return self.abbr

    def from_si(self, value: Decimal) -> Decimal:
        """
        Converts a value from SI units using the linear transformation.

        Args:
            value (Decimal): The value in SI units.

        Returns:
            Decimal: The value converted to the custom unit.
        """
        return (value - self.c) / self.m

    def to_si(self, value: Decimal) -> Decimal:
        """
        Converts a value to SI units using the inverse of the linear transformation.

        Args:
            value (Decimal): The value in the custom unit.

        Returns:
            Decimal: The value converted to SI units.
        """
        return value * self.m + self.c


class ProportionalUnit(LinearUnit):
    """
    Represents a proportional unit of measurement, which is a special case
    of a linear unit with zero offset (c = 0).

    The transformation simplifies to:
        y = m * x
    """
    def __init__(self, name: str, abbr: str, m: Decimal):
        """
        Initializes the proportional unit with a name, abbreviation, and scale.

        Args:
            name (str): The full name of the unit.
            abbr (str): The unit abbreviation.
            m (Decimal): The scaling factor.
        """
        super().__init__(name, abbr, m, Decimal(0))


class UnitCategory:
    def __init__(self, name: str):
        """
        Initializes a unit category and creates an empty list of Unit objects sorted by name.

        Args:
            name (str): The name of the unit category instance to add.
        """
        self.name = name
        self.units: list[Unit] = []

    def get_name(self):
        """
        Returns the name of the unit category.

        Returns:
            str: The name of the unit category.
        """
        return self.name

    def get_units(self) -> list[Unit]:
        """
        Returns the units belonging to the unit category.

        Returns:
            list[Unit]: The list of the units belonging to the unit category.
        """
        return self.units

    def add_unit(self, unit: Unit):
        """
        Adds a unit to the category, maintaining alphabetical order by unit name.

        Args:
            unit (Unit): The unit instance to add.
        """
        names = [u.get_name() for u in self.units]
        index = bisect.bisect_left(names, unit.get_name())
        self.units.insert(index, unit)


def load_units(filepath: Path) -> list[UnitCategory]:
    units = []
    with open(filepath, "r") as f:
        unit_definitions = load(f)
        for unit_category_name in unit_definitions:
            unit_category = UnitCategory(unit_category_name)
            for unit_definition in unit_definitions[unit_category_name]:
                if unit_definition["unitType"] == "proportional":
                    unit = ProportionalUnit(
                        unit_definition["name"],
                        unit_definition["abbr"],
                        Decimal(unit_definition["conversionFactors"]["m"])
                    )
                    unit_category.add_unit(unit)
            units.append(unit_category)
    return units


def convert(value: Decimal, from_unit: Unit, to_unit: Unit) -> Decimal:
    """
    Converts a numerical value from one unit to another using an intermediate SI representation.

    Args:
        value (Decimal): The value to convert.
        from_unit (Unit): The unit to convert from.
        to_unit (Unit): The unit to convert to.

    Returns:
        Decimal: The value converted to the target unit.
    """
    return to_unit.from_si(from_unit.to_si(value))
