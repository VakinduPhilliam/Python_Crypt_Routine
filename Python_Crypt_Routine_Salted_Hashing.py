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
# In BLAKE2 the salt is processed as a one-time input to the hash function during initialization, rather than as an input to each
# compression function.
# 
# Warning:
# 
# Salted hashing (or just hashing) with BLAKE2 or any other general-purpose cryptographic hash function, such as SHA-256, is not
# suitable for hashing passwords. See BLAKE2 FAQ for more information.
# 

import os
from hashlib import blake2b

msg = b'some message'

# Calculate the first hash with a random salt.

salt1 = os.urandom(blake2b.SALT_SIZE)

h1 = blake2b(salt=salt1)
h1.update(msg)

# Calculate the second hash with a different random salt.

salt2 = os.urandom(blake2b.SALT_SIZE)

h2 = blake2b(salt=salt2)
h2.update(msg)

# The digests are different.

h1.digest() != h2.digest()

#
# OUTPUT:
#
# True
#