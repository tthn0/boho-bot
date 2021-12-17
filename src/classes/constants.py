from dotenv import load_dotenv
import os


load_dotenv()


class CONSTANTS:
    TOKEN: str = os.getenv("TOKEN")
    GUILD_ID: int = int(os.getenv("GUILD_ID"))
    CHANNEL_ID: int = int(os.getenv("CHANNEL_ID"))
