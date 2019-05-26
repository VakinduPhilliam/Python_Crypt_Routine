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
# Personalization.
# Sometimes it is useful to force hash function to produce different digests for the same input for different purposes.
# BLAKE2 can be personalized by passing bytes to the person argument:
 
from hashlib import blake2b

FILES_HASH_PERSON = b'MyApp Files Hash'
BLOCK_HASH_PERSON = b'MyApp Block Hash'

h = blake2b(digest_size=32, person=FILES_HASH_PERSON)
h.update(b'the same content')

h.hexdigest()

#
# OUTPUT:
#
# '20d9cd024d4fb086aae819a1432dd2466de12947831b75c5a30cf2676095d3b4'
#

h = blake2b(digest_size=32, person=BLOCK_HASH_PERSON)
h.update(b'the same content')

h.hexdigest()

#
# OUTPUT:
#
# 'cf68fb5761b9c44e7878bfb2c4c9aea52264a80b75005e65619778de59f383a3'
#