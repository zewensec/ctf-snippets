import hashlib

# Hash value that we're looking for
correctHash = "e82a4b4a0386d5232d52337f36d2ab73"

for num in range(00000, 99999):
    hashToCheck = "ctflag" + str(num)
    candidateHash = (hashlib.md5(str(hashToCheck).encode('utf-8')).hexdigest())
    if candidateHash == correctHash:
        print("Found correct hash! \n" + candidateHash + "\nThe password is: " +
              hashToCheck)
