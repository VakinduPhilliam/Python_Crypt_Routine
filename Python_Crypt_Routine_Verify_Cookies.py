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
# A web application can symmetrically sign cookies sent to users and later verify them to make sure they weren’t tampered with:
# 

from hashlib import blake2b
from hmac import compare_digest

SECRET_KEY = b'pseudorandomly generated server secret key'
AUTH_SIZE = 16

    def sign(cookie):
        h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
        h.update(cookie)

        return h.hexdigest().encode('utf-8')

    def verify(cookie, sig):
        good_sig = sign(cookie)
        return compare_digest(good_sig, sig)

    cookie = b'user-alice'
    sig = sign(cookie)

    print("{0},{1}".format(cookie.decode('utf-8'), sig))

#
# OUTPUT:
#
# user-alice,b'43b3c982cf697e0c5ab22172d1ca7421'
#

verify(cookie, sig)

#
# OUTPUT:
#
# True
#

verify(b'user-bob', sig)

#
# OUTPUT:
#
# False
#

verify(cookie, b'0102030405060708090a0b0c0d0e0f00')

#
# OUTPUT:
#
# False
#