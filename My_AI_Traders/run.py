# run.py
from dotenv import load_dotenv
load_dotenv()  # This line loads environment variables from .env file at the start

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
