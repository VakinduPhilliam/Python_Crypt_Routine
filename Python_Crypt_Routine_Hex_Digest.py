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
# Even though there’s a native keyed hashing mode, BLAKE2 can, of course, be used in HMAC construction with hmac module:
 
import hmac, hashlib

m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'message')

m.hexdigest()

# 
# OUTPUT:
#
# 'e3c8102868d28b5ff85fc35dda07329970d1a01e273c37481326fe0c861c8142'
#