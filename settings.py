import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    print("**You are in a debugging environment!")
    from pathlib import Path
    from dotenv import load_dotenv # For docker later on
    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files.development import *
else:
    print("**You are in a production environment!")
    from settings_files.production import *
