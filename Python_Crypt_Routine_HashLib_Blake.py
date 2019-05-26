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
# You can pass the first chunk of data to update directly to the constructor as the positional argument:
# 

from hashlib import blake2b

blake2b(b'Hello world').hexdigest()

#
# OUTPUT:
#
# '6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
#