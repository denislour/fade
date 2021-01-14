from src.app.user import models, schemas
from src.app.core.services import BaseService, PasswordCryptService


class UserService(BaseService, PasswordCryptService):
    """[summary]

    Args:
        BaseService ([type]): [description]
        PasswordCryptService ([type]): [description]

    Returns:
        [type]: [description]
    """
    model = models.User
    create_schema = schemas.UserCreateInRegistration
    update_schema = schemas.UserUpdate
    get_schema = schemas.User_G_Pydantic

    async def create_user(self, schema: schemas.UserCreateInRegistration, **kwargs):

        hash_password = self.get_password_hash(schema.dict().pop('password'))
        return await self.create(schemas.UserCreateInRegistration(
            **schema.dict(exclude={"password"}), password=hash_password, **kwargs
        ))


user_service = UserService()
