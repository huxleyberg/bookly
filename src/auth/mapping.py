from src.auth.models import User
from src.auth.schemas import UserModel


def to_user_model(user: User) -> UserModel:
    return UserModel(
        uid=user.uid,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_verified=user.is_verified,
        created_at=user.created_at,
        update_at=user.update_at,
        # password_hash will be excluded automatically by Pydantic's `Field(exclude=True)`
    )
