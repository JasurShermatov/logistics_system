"""Auth service - login, token yangilash."""
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import UserRepository
from core.security import verify_password, create_access_token, create_refresh_token, hash_password
from schemas.auth import TokenResponse, RegisterRequest
from models.user import User, RoleEnum
from typing import Optional


class AuthService:
    """Auth logika."""
    
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)
    
    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """User login tekshirish."""
        user = await self.user_repo.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    async def login(self, email: str, password: str) -> Optional[TokenResponse]:
        """Login va token yaratish."""
        user = await self.authenticate_user(email, password)
        if not user:
            return None
        access_token = create_access_token({"sub": str(user.id), "role": user.role.value})
        refresh_token = create_refresh_token({"sub": str(user.id), "role": user.role.value})
        return TokenResponse(access_token=access_token, refresh_token=refresh_token)
    
    async def register(self, data: RegisterRequest) -> User:
        """User registratsiyasi."""
        user_data = {
            "email": data.email,
            "full_name": data.full_name,
            "hashed_password": hash_password(data.password),
            "phone": data.phone,
            "role": RoleEnum.DRIVER,
            "is_active": True,
        }
        return await self.user_repo.create(user_data)
