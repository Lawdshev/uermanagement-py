import json
import bcrypt
from pathlib import Path

DB_FILE = Path(__file__).parent / "db" / "users.json"

def read_users():
    if not DB_FILE.exists():
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=2)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
