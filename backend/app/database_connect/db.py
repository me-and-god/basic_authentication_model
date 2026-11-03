""" This file is to get the database secret Database URL from the .env file """

from dotenv import load_dotenv
import os



load_dotenv()

DBUrl = os.getenv("DB_URL")
