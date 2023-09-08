from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding='utf-8',
    )

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str


class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv('.env_jwt'),
        env_file_encoding='utf-8',
    )

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


db_settings = DBSettings()
jwt_settings = JWTSettings()