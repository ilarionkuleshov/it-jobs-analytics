"""Settings for the project from environment variables."""

import dotenv
import pydantic_settings


class DatabaseSettings(pydantic_settings.BaseSettings):
    """Settings for the database."""

    url: str

    model_config = pydantic_settings.SettingsConfigDict(
        env_file=dotenv.find_dotenv(),
        extra="ignore",
        env_prefix="database_",
    )

    def get_url(self) -> str:
        """Returns connection URL for the database.

        Note:
            At the moment, this method simply returns `url` attribute,
            but in the future, when switching to another database (not SQLite),
            real logic for building URL for connecting to the database can be implemented here.

        """
        return self.url
