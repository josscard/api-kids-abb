"""
Binary Search Tree implementation for managing kids.
Provides basic BST operations: insert, search, delete, inorder traversal.
"""
from typing import List, Optional
from .kid_model import KidNode


class KidsBinarySearchTree:
    """
    Binary Search Tree implementation for storing and managing kids.
    The tree is ordered by kid_id for efficient searching.
    """

    def __init__(self):
        self.root: Optional[KidNode] = None
        self._node_count = 0

    def insert(self, kid_id: int, name: str, age: int) -> bool:
        """
        Insert a new kid into the BST.
        Returns True if inserted successfully, False if kid_id already exists.
        """
        new_node = KidNode(kid_id, name, age)

        if self.root is None:
            self.root = new_node
            self._node_count += 1
            return True

        return self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current: KidNode, new_node: KidNode) -> bool:
        """Recursive helper for insertion."""
        if new_node.kid_id < current.kid_id:
            if current.left is None:
                current.left = new_node
                self._node_count += 1
                return True
            else:
                return self._insert_recursive(current.left, new_node)
        elif new_node.kid_id > current.kid_id:
            if current.right is None:
                current.right = new_node
                self._node_count += 1
                return True
            else:
                return self._insert_recursive(current.right, new_node)
        else:
            # Duplicate kid_id
            return False

    def search(self, kid_id: int) -> Optional[KidNode]:
        """Search for a kid by kid_id."""
        return self._search_recursive(self.root, kid_id)

    def _search_recursive(self, current: Optional[KidNode], kid_id: int) -> Optional[KidNode]:
        """Recursive helper for search."""
        if current is None or current.kid_id == kid_id:
            return current

        if kid_id < current.kid_id:
            return self._search_recursive(current.left, kid_id)
        else:
            return self._search_recursive(current.right, kid_id)

    def delete(self, kid_id: int) -> bool:
        """Delete a kid from the BST."""
        if self._delete_recursive(self.root, kid_id):
            self._node_count -= 1
            return True
        return False

    def _delete_recursive(self, current: Optional[KidNode], kid_id: int) -> Optional[KidNode]:
        """Recursive helper for deletion."""
        if current is None:
            return None

        if kid_id < current.kid_id:
            current.left = self._delete_recursive(current.left, kid_id)
        elif kid_id > current.kid_id:
            current.right = self._delete_recursive(current.right, kid_id)
        else:
            # Node to delete found
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Node with two children, find inorder successor
            successor = self._find_min(current.right)
            current.kid_id = successor.kid_id
            current.name = successor.name
            current.age = successor.age
            current.right = self._delete_recursive(current.right, successor.kid_id)

        return current

    def _find_min(self, node: KidNode) -> KidNode:
        """Find the minimum value node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self) -> List[KidNode]:
        """Return inorder traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[KidNode], result: List[KidNode]):
        """Recursive helper for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node)
            self._inorder_recursive(node.right, result)

    def get_size(self) -> int:
        """Return the number of nodes in the tree."""
        return self._node_count

    def is_empty(self) -> bool:
        """Check if the tree is empty."""
        return self._node_count == 0
