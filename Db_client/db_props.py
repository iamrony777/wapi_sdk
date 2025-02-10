from dotenv import load_dotenv
import os

class DBPropertyUtil:
    @staticmethod
    def getParameter():
        load_dotenv()  # Load variables from .env
        return {
            "host": os.getenv("DB_HOST"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD")
        }

    @staticmethod
    def getConnUrl():
        load_dotenv()
        return os.getenv("DB_URL")