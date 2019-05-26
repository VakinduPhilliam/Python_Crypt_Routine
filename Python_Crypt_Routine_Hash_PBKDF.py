# Python Crypt Routine
# crypt — Function to check Unix passwords.
# This module implements an interface to the crypt(3) routine, which is a one-way hash function based upon
# a modified DES algorithm; see the Unix man page for further details.
# Possible uses include storing hashed passwords so you can check passwords without storing the actual password,
# or attempting to crack Unix passwords with a dictionary.
# Notice that the behavior of this module depends on the actual implementation of the crypt(3) routine in the running system.
# Therefore, any extensions available on the current implementation will also be available on this module.
# hashlib — Secure hashes and message digests.
# This module implements a common interface to many different secure hash and message digest algorithms.
# Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, and SHA512 (defined in FIPS 180-2) as well as RSA’s
# MD5 algorithm (defined in Internet RFC 1321). The terms “secure hash” and “message digest” are interchangeable.
# Older algorithms were called message digests. The modern term is secure hash.
# Hash algorithms.
# There is one constructor method named for each type of hash. All return a hash object with the same simple interface.
# hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None). 
# The function provides PKCS#5 password-based key derivation function 2.
# It uses HMAC as pseudorandom function.
# The string hash_name is the desired name of the hash digest algorithm for HMAC, e.g. ‘sha1’ or ‘sha256’.
# password and salt are interpreted as buffers of bytes. Applications and libraries should limit password to a sensible length (e.g. 1024).
# salt should be about 16 or more bytes from a proper source, e.g. os.urandom().
# The number of iterations should be chosen based on the hash algorithm and computing power. As of 2013, at least 100,000 iterations of SHA-256
# are suggested.
# dklen is the length of the derived key. If dklen is None then the digest size of the hash algorithm hash_name is used, e.g. 64 for SHA-512.
 
import hashlib, binascii

dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
binascii.hexlify(dk)

#
# OUTPUT:
#
# b'0394a2ede332c9a13eb82e9b24631604c31df978b4e2f0fbd2c549944f9d79a5'
