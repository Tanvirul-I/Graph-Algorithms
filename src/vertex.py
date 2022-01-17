from dataclasses import dataclass
from typing import Type

@dataclass
class Vertex:
    value: str

@dataclass
class VertexAdj:
    value: Type['Vertex']
    nextAdj: Type['VertexAdj']
    weight: int