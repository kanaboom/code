from pydantic import BaseSettings

class ServerEnve(BaseSettings):
    postgres_host:str
    postgres_port:str
    postgres_user:str
    postgres_pass:str
    postgres_db:str