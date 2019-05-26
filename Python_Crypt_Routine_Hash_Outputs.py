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
# Hash objects with different digest sizes have completely different outputs (shorter hashes are not prefixes of longer hashes);
# BLAKE2b and BLAKE2s produce different outputs even if the output length is the same:
 
from hashlib import blake2b, blake2s

blake2b(digest_size=10).hexdigest()

#
# OUTPUT:
#
# '6fa1d8fcfd719046d762'
#

blake2b(digest_size=11).hexdigest()

#
# OUTPUT:
#
# 'eb6ec15daf9546254f0809'
#

blake2s(digest_size=10).hexdigest()

#
# OUTPUT:
#
# '1bf21a98c78a1c376ae9'
#

blake2s(digest_size=11).hexdigest()

#
# OUTPUT:
#
# '567004bf96e4a25773ebf4'
#