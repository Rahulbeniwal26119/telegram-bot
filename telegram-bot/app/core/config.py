
from typing import List, Union
import simplejson as json


from pydantic import AnyHttpUrl, BaseSettings, validator

class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    BOT_TOKEN: str = ''

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

try:
    import pathlib
    fp = pathlib.Path("../../confidentals.json").open()
    secrets = json.load(fp, 'utf-8')
    print("secrets", secrets)
    settings.BOT_TOKEN = secrets["telegram_bot_token"]
except Exception as e:
    print(e)
else:
    fp.close()
