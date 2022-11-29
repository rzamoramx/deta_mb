
import os
from pydantic import BaseSettings


class DetaDBSettings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = './dev.env'  # if os.getenv("DEV") is None else './prod.env'


detadb_settings = DetaDBSettings()
