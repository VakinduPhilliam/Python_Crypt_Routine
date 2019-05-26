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
#
# Personalization together with the keyed mode can also be used to derive different keys from a single one.
# 

from hashlib import blake2s
from base64 import b64decode, b64encode

orig_key = b64decode(b'Rm5EPJai72qcK3RGBpW3vPNfZy5OZothY+kHY6h21KM=')

enc_key = blake2s(key=orig_key, person=b'kEncrypt').digest()
mac_key = blake2s(key=orig_key, person=b'kMAC').digest()

print(b64encode(enc_key).decode('utf-8'))

#
# OUTPUT:
#
# rbPb15S/Z9t+agffno5wuhB77VbRi6F9Iv2qIxU7WHw=
#

print(b64encode(mac_key).decode('utf-8'))

#
# OUTPUT:
#
# G9GtHFE1YluXY1zWPlYk1e/nWfu0WSEb0KRcjhDeP/o=
#