from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import urllib.parse
import base64

def byte_to_string(val_in_bytes):
    val_as_string = val_in_bytes.decode()
    return val_as_string

def string_to_byte(val_as_string):
    val_in_bytes = val_as_string.encode()
    return val_in_bytes

def quote_string(unquoted_string):
    quoted_string = urllib.parse.quote(unquoted_string)
    return quoted_string

def unquote_string(quoted_string):
    unquoted_string = urllib.parse.unquote(quoted_string)
    return unquoted_string

def encrypt(message):
    # set public key path 
    public_key_path = './public_key_1024.pem'
    public_key = RSA.importKey(open(public_key_path, 'r').read())
    # creating the RSA object using public key
    rsa_object = PKCS1_v1_5.new(public_key)
    
    # encrypt the message 
    cipher_text = rsa_object.encrypt(message.encode())
    
    # encode the ciphertext to bas
    cipher_text = base64.b64encode(cipher_text)
    
    # quote cipher_text if you are dealing with URL params 
    cipher_text = quote_string(cipher_text)
    return cipher_text


def decrypt(cipher_text):
    
    #just unquote the data if it's quoted 
    cipher_text = unquote_string(cipher_text)
    
    # decode the cipher_text to base64
    cipher_text = base64.b64decode(cipher_text)
    # set private key path 
    private_key_path='./private_key_1024.pem'
    private_key = RSA.importKey(open(private_key_path, 'r').read())
    
    # creating the RSA object using private key
    rsa_object = PKCS1_v1_5.new(private_key)
    
    # signature is passed as None, it ensures the data integrity be
    # our goal is data security for the moment so signature is None
    plain_text = rsa_object.decrypt(cipher_text, None).decode()
    return plain_text

if __name__ == '__main__':
    print("-----------RSA Encryption-----------")
    plain_text = input("Enter the plain text to encrypt :")
    print()
    cipher_text = encrypt(plain_text)
    print("Cipher Text is : {}".format(cipher_text))
    print()
    plain_text = decrypt(cipher_text)
    print("Plain Text is : {}".format(plain_text))