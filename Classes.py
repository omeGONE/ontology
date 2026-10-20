from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    name: str


@dataclass
class Discipline(Root):
    description: str


@dataclass
class Bike(Root):
    createdFor: Discipline


@dataclass
class Component(Root):
    isPart: Union['Component', 'ComponentGroup', 'Bike'] = field(default_factory=list)


@dataclass
class ComponentGroup(Root):
    isPart: 'Bike' = field(default_factory=list)


@dataclass
class BrakeSystem(ComponentGroup):
    pass


@dataclass
class Drivetrain(ComponentGroup):
    pass


@dataclass
class Fork(Component):
    pass


@dataclass
class Cassette(Component):
    hasSprocket: List['Sprocket'] = field(default_factory=list)


@dataclass
class Sprocket(Component):
    pass


@dataclass
class BrakeRotor(Component):
    pass


@dataclass
class BrakeCaliper(Component):
    pass


@dataclass
class BrakeLever(Component):
    pass


@dataclass
class Derailleur(Component):
    pass


@dataclass
class Shifter(Component):
    pass