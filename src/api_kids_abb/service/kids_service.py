"""
Service layer for kids ABB operations.
Contains business logic for managing the binary search tree.
"""
from typing import List, Optional
from ..model.kid_model import KidNode, KidCreate, KidResponse
from ..model.binary_search_tree import KidsBinarySearchTree


class KidsService:
    """
    Service class for managing kids in the ABB.
    Handles business logic and coordinates with the BST model.
    """

    def __init__(self):
        self.tree = KidsBinarySearchTree()
        self._next_id = 1  # Contador para IDs cortos

    def add_kid(self, kid_data: KidCreate) -> bool:
        """
        Add a new kid to the tree.
        Validates that the kid doesn't already exist.
        """
        # Usar un ID incremental corto
        kid_id = self._next_id
        self._next_id += 1

        return self.tree.insert(kid_id, kid_data.name, kid_data.age)

    def get_kid(self, kid_id: int) -> Optional[KidResponse]:
        """Get a kid by their ID."""
        kid_node = self.tree.search(kid_id)
        if kid_node is None:
            return None

        return KidResponse(
            kid_id=kid_node.kid_id,
            name=kid_node.name,
            age=kid_node.age
        )

    def get_all_kids(self) -> List[KidResponse]:
        """Get all kids in inorder traversal."""
        nodes = self.tree.inorder_traversal()
        return [
            KidResponse(kid_id=node.kid_id, name=node.name, age=node.age)
            for node in nodes
        ]

    def remove_kid(self, kid_id: int) -> bool:
        """Remove a kid from the tree."""
        return self.tree.delete(kid_id)

    def get_tree_size(self) -> int:
        """Get the total number of kids in the tree."""
        return self.tree.get_size()

    def is_tree_empty(self) -> bool:
        """Check if the tree is empty."""
        return self.tree.is_empty()
