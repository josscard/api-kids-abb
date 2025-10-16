"""
Kid model for the Binary Search Tree implementation.
Represents a child node in the ABB (Árbol Binario de Búsqueda).
"""
from typing import Optional
from pydantic import BaseModel


class KidNode:
    """
    Node class representing a kid in the binary search tree.
    Each node contains kid information and references to left/right children.
    """

    def __init__(self, kid_id: int, name: str, age: int):
        self.kid_id = kid_id
        self.name = name
        self.age = age
        self.left: Optional['KidNode'] = None
        self.right: Optional['KidNode'] = None

    def __repr__(self):
        return f"KidNode(id={self.kid_id}, name='{self.name}', age={self.age})"


class KidCreate(BaseModel):
    """Schema for creating a new kid."""
    name: str
    age: int


class KidResponse(BaseModel):
    """Schema for kid response."""
    kid_id: int
    name: str
    age: int
