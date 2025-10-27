from typing import List
from fastapi import Depends, HTTPException, Request, status
from app.core.factory import Factory
from app.services.user import UserService


def require_roles(allowed_roles: List[str]):
    async def role_checker(
        request: Request,
        user_service: UserService = Depends(Factory.get_user_service),
    ):
        if not request.user.is_authenticated:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        user = user_service.get_by_id(request.user.id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not user.role or user.role.name not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        
        return user
    
    return role_checker
