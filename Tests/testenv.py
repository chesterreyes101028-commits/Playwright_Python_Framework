from encodings.punycode import T
import os
from dotenv import load_dotenv,dotenv_values

dotenv_values()

print(os.getenv("Base_URL"))
print(os.getenv("Username"))
print(os.getenv("Password"))