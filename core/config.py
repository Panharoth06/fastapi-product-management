# core/cofig.py

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field
from keycloak import KeycloakOpenID

# Load the .env file
load_dotenv()

# Read environment variables
DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# Construct the full database URL
DATABASE_URL = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


class Settings(BaseSettings):
    keycloak_server_url: str = Field(..., env="KEYCLOAK_SERVER_URL")
    keycloak_realm: str = Field(..., env="KEYCLOAK_REALM")
    keycloak_client_id: str = Field(..., env="KEYCLOAK_CLIENT_ID")
    keycloak_client_secret: str = Field(..., env="KEYCLOAK_CLIENT_SECRET")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}
    
settings = Settings()
keycloak_openid = KeycloakOpenID(
    server_url=settings.keycloak_server_url,
    realm_name=settings.keycloak_realm,
    client_id=settings.keycloak_client_id,
    client_secret_key=settings.keycloak_client_secret,
)
