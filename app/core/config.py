from pydantic_settings import BaseSettings
import dotenv

dotenv.load_dotenv()

class Settings(BaseSettings):
    # Database configuration
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_HOST: str

    class Config:
        """
        The `Config` class defines the configuration options for the `Settings` class.

        Attributes:
        - case_sensitive: A boolean indicating whether the configuration options are case sensitive.
        """
        case_sensitive = True


settings = Settings()
