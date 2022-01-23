import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "0100000002d6b7a8467d9e75f77578b5b6970b6b9ba19be509bccd351120d1f1c717ea934f040000008a4730440220573351861d3f6a785f28ff905b137901e46f9fd737c8caf05b808ed6a67a41090220512d31016b88b64d084ea7c2962aaf64a311032932b79f19950ef3531af86d050141042a6fd5fcaa79f430815b859d5532d5277dc019874105af1f9f51bdb0a97c54ceb374dbfd107b54568f50d27aea5adfce89897f1ba68453b8b910c5f0e5ef4f6dffffffff4105c25b1d89481fe99b29a9396d56e22dc741cd69d930ac2385e26ebc4a9ae0050000008c4930460221009328a0a7e2b3c8fcc74e02d2bb3dc6d1e53d7b071288e4d3ca8d5d9f8d354adf022100da18d7ce0f1510393c4282aacc9639ed44bd9d64e551604e0e4bf503dd5be3030141042a6fd5fcaa79f430815b859d5532d5277dc019874105af1f9f51bdb0a97c54ceb374dbfd107b54568f50d27aea5adfce89897f1ba68453b8b910c5f0e5ef4f6dffffffff0280b63908000000001976a914fb6d7e9de35729eb321ebce4e5fab32f55d84e2a88acfd1e5d01000000001976a914a8f511a2752b6bb5eb1203cbae1149696642f6bc88ac00000000"
m = txnUtils.parseTxn(tx)
e = txnUtils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')
s = keyUtils.derSigToHexSig(m[1][:-2])
pub =  m[2]
sigR = s[:64]
sigS = s[-64:]
sigZ = z
print ('Signed TX is :', tx)
print ('Signature (r, s pair) is :', s)
print ('Public Key is :', pub)
print ("")
print ("#################################################################################################")
print ("")
print ('Unsigned TX is :', e)
print ('hash of message (sigZ) is USE This ONE :', z)
print ('reversed z :', z1)
print ("")
print ("#################################################################################################")
print ("##################################VALUES NEEDED ARE BELOW #######################################")
print ("#################################################################################################")
print ("")
print ('THE R VALUE is  :', sigR)
print ('THE S VALUE is  :', sigS)
print ('THE Z VALUE is  :', sigZ)
print ('THE PUBKEY is :', pub)


