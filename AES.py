from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib
iv="vyLlwWSY1PCK5ELNTPUVdpl8z0rIXiB2+Ybcu/BeXidR3MEiym852HCkS6wHVCr+CdpP6Moe9VQUeFcyq3vZDpVK/orl+8vREYMRrnQR9O4="
BLOCK_SIZE = 16
hashs= "bbb2c5e63d2ef893106fdd0d797aa97a"
secret = b'not_the_secret'
key = hashlib.sha256()
key.update(secret)
secret2 = key.digest()
def encrypt(message, passphrase):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return base64.b64encode(aes.encrypt(message))

def decrypt(encrypted, passphrase):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(encrypted))
print len(hashs)
print decrypt(hashs.decode("hex"), secret2 )