
import os
from pydantic import BaseSettings


class DetaDBSettings(BaseSettings):
    API_KEY: int

    class Config:
        env_file = './dev.env' if os.getenv("CLOUD") is None else './cloud.env'


detadb_settings = DetaDBSettings()
