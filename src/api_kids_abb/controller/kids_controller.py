"""
Controller for kids ABB API endpoints.
Handles HTTP requests and coordinates with the service layer.
"""
from typing import List
from fastapi import HTTPException, status
from ..model.kid_model import KidCreate, KidResponse
from ..service.kids_service import KidsService


class KidsController:
    """
    Controller class for managing kids API endpoints.
    Coordinates between HTTP layer and business logic.
    """

    def __init__(self):
        self.kids_service = KidsService()

    def health_check(self) -> dict:
        """Health check endpoint."""
        return {"status": "ok"}

    def add_kid(self, kid_data: KidCreate) -> dict:
        """
        Add a new kid to the tree.
        """
        success = self.kids_service.add_kid(kid_data)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Kid with this information already exists"
            )

        return {
            "message": "Kid added successfully",
            "kid": {
                "name": kid_data.name,
                "age": kid_data.age
            }
        }

    def get_kid(self, kid_id: int) -> KidResponse:
        """
        Get a kid by their ID.
        """
        kid = self.kids_service.get_kid(kid_id)
        if kid is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Kid with ID {kid_id} not found"
            )

        return kid

    def get_all_kids(self) -> List[KidResponse]:
        """
        Get all kids in the tree (inorder traversal).
        """
        return self.kids_service.get_all_kids()

    def remove_kid(self, kid_id: int) -> dict:
        """
        Remove a kid from the tree.
        """
        success = self.kids_service.remove_kid(kid_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Kid with ID {kid_id} not found"
            )

        return {"message": f"Kid with ID {kid_id} removed successfully"}

    def get_tree_stats(self) -> dict:
        """
        Get statistics about the tree.
        """
        return {
            "total_kids": self.kids_service.get_tree_size(),
            "is_empty": self.kids_service.is_tree_empty()
        }
