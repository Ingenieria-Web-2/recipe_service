"""
Recipe API router.
"""

from fastapi import APIRouter, Depends

from app.api import dependencies
from app.schemas import recipe_schema
from app.services.recipe_service import RecipeService

router = APIRouter()


@router.post("/create", response_model=recipe_schema.Recipe)
def create_recipe(
    recipe_in: recipe_schema.RecipeCreate,
    service: RecipeService = Depends(),
    current_user_id: int = Depends(dependencies.get_current_user_id)
):
    """
    Create a new recipe. The owner is the currently authenticated user.
    """
    return service.create_new_recipe(recipe_in=recipe_in, owner_id=current_user_id)
