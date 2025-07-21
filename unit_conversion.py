from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Abstract base class representing a unit of measurement.

    Subclasses must implement conversion to and from SI (International System of Units).
    """
    @abstractmethod
    def from_si(self, value: float) -> float:
        """
        Converts a value from SI units to this unit.

        Args:
            value (float): The value in SI units.

        Returns:
            float: The value converted to this unit.
        """
        ...

    @abstractmethod
    def to_si(self, value: float) -> float:
        """
        Converts a value from this unit to SI units.

        Args:
            value (float): The value in this unit.

        Returns:
            float: The value converted to SI units.
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
    def __init__(self, m: float, c: float):
        """
        Initializes the linear unit with a scale and offset.

        Args:
            m (float): The scaling factor.
            c (float): The offset value.
        """
        self.m = m
        self.c = c

    def from_si(self, value: float) -> float:
        """
        Converts a value from SI units using the linear transformation.

        Args:
            value (float): The value in SI units.

        Returns:
            float: The value converted to the custom unit.
        """
        return (value - self.c) / self.m

    def to_si(self, value: float) -> float:
        """
        Converts a value to SI units using the inverse of the linear transformation.

        Args:
            value (float): The value in the custom unit.

        Returns:
            float: The value converted to SI units.
        """
        return value * self.m + self.c


class ProportionalUnit(LinearUnit):
    """
    Represents a proportional unit of measurement, which is a special case
    of a linear unit with zero offset (c = 0).

    The transformation simplifies to:
        y = m * x
    """
    def __init__(self, m: float):
        """
        Initializes the proportional unit with a scale.

        Args:
            m (float): The scaling factor.
        """
        super().__init__(m, 0)


def convert(value: float, from_unit: Unit, to_unit: Unit) -> float:
    """
    Converts a numerical value from one unit to another using an intermediate SI representation.

    Args:
        value (float): The value to convert.
        from_unit (Unit): The unit to convert from.
        to_unit (Unit): The unit to convert to.

    Returns:
        float: The value converted to the target unit.
    """
    return to_unit.from_si(from_unit.to_si(value))
