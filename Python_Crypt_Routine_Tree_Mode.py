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
# Tree mode.
# 
# An example of hashing a minimal tree with two leaf nodes:
# 
# This example uses 64-byte internal digests, and returns the 32-byte final digest:
# 

from hashlib import blake2b

FANOUT = 2
DEPTH = 2

LEAF_SIZE = 4096
INNER_SIZE = 64

buf = bytearray(6000)

# Left leaf

h00 = blake2b(buf[0:LEAF_SIZE], fanout=FANOUT, depth=DEPTH,
                  leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
                  node_offset=0, node_depth=0, last_node=False)

# Right leaf

h01 = blake2b(buf[LEAF_SIZE:], fanout=FANOUT, depth=DEPTH,
                  leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
                  node_offset=1, node_depth=0, last_node=True)

# Root node

h10 = blake2b(digest_size=32, fanout=FANOUT, depth=DEPTH,
                  leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
                  node_offset=0, node_depth=1, last_node=True)

    h10.update(h00.digest())
    h10.update(h01.digest())

    h10.hexdigest()

#
# OUTPUT:
#
# '3ad2a9b37c6070e374c7a8c508fe20ca86b6ed54e286e93a0318e95e881db5aa'
#