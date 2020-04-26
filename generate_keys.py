from Crypto.PublicKey import RSA

def generate_keys(key_size):
	
	# generating a key pair of public and private key for given size 
	key_pair = RSA.generate(key_size)

	# storing private key in file name as private_key_{keysize}.pem file
	file_obj = open("private_key_"+str(key_size)+".pem", "wb")
	file_obj.write(key_pair.exportKey('PEM'))
	file_obj.close()

	#storing public key in file name as public_key_{keysize}.pem file
	pubkey = key_pair.publickey()
	file_obj = open("public_key_"+str(key_size)+".pem", "wb")
	file_obj.write(pubkey.exportKey('OpenSSH'))
	file_obj.close()

if __name__ == '__main__':
	key_size = 1024
	generate_keys(key_size)