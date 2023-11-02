from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str
    DB_URI: str
    EMAIL: str
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_LOGIN: str
    SMTP_PASSWORD: str
    SMTP_EMAIL: str

    class Config:
        env_file = './.env'


settings = Settings()
