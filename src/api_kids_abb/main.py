"""
Main FastAPI application for the Kids ABB API.
"""
from fastapi import FastAPI
from .controller.kids_controller import KidsController
from .model.kid_model import KidCreate

# Initialize the controller
kids_controller = KidsController()

# Create FastAPI application
app = FastAPI(
    title="Kids ABB API",
    description="API for managing kids in a Binary Search Tree",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return kids_controller.health_check()


@app.post("/api/v1/kids/add")
def add_kid(kid_data: KidCreate):
    """Add a new kid to the tree."""
    return kids_controller.add_kid(kid_data)


@app.get("/api/v1/kids/list")
def get_all_kids():
    """Get all kids in the tree."""
    return kids_controller.get_all_kids()


@app.get("/api/v1/kids/stats")
def get_tree_stats():
    """Get tree statistics."""
    return kids_controller.get_tree_stats()


@app.get("/api/v1/kids/{kid_id}")
def get_kid(kid_id: int):
    """Get a kid by their ID."""
    return kids_controller.get_kid(kid_id)


@app.delete("/api/v1/kids/{kid_id}")
def remove_kid(kid_id: int):
    """Remove a kid from the tree."""
    return kids_controller.remove_kid(kid_id)
