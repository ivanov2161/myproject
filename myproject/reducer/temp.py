import string
import secrets
alphabet = string.ascii_letters + string.digits
key = ''.join(secrets.choice(alphabet) for i in range(5))



