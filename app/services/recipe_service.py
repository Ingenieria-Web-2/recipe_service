"""
Recipe service for business logic related to recipes.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.recipe_model import Recipe
from app.repositories.recipe_repository import RecipeRepository
from app.schemas.recipe_schema import RecipeCreate


class RecipeService:
    """
    Recipe service for business logic related to recipes.
    """

    def __init__(self, db: Session = Depends(get_db)):
        self.repo = RecipeRepository(db)

    def create_new_recipe(self, *, recipe_in: RecipeCreate, owner_id: int) -> Recipe:
        """
        Create a new recipe.
        """
        return self.repo.create_recipe(recipe_in=recipe_in, owner_id=owner_id)
