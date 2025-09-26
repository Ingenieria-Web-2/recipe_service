"""
Recipe repository for database interactions.
"""

from sqlalchemy.orm import Session

from app.models.recipe_model import Recipe
from app.schemas.recipe_schema import RecipeCreate


class RecipeRepository:
    """
    Recipe repository for database interactions.
    """

    def __init__(self, db: Session):
        self.db = db

    def create_recipe(self, *, recipe_in: RecipeCreate, owner_id: int) -> Recipe:
        """
        Create a new recipe in the database.
        """
        db_recipe = Recipe(
            **recipe_in.model_dump(),
            owner_id=owner_id
        )
        self.db.add(db_recipe)
        self.db.commit()
        self.db.refresh(db_recipe)
        return db_recipe

    def get_recipe_by_id(self, recipe_id: int) -> Recipe | None:
        """
        Retrieve a recipe by its ID.
        """
        return self.db.query(Recipe).filter(Recipe.id == recipe_id).first()
