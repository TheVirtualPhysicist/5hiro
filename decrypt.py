from cryptography.fernet import Fernet
import os

key = os.environ['FERNET']
fernet = Fernet(key)

# decrypting
print("Loading crypted strategies...")
f = open("Strategies.enc","rb")
text = f.read()
f.close()
f = open("Strategies.py","wb")
f.write(fernet.decrypt(text))
f.close()
print("Strategies decrypted.")

# decrypting
# print("Loading crypted model...")
# f = open("cmodel.pkl","rb")
# text = f.read()
# f.close()
# f = open("model.pkl","wb")
# f.write(fernet.decrypt(text))
# f.close()
# print("Model decrypted.")