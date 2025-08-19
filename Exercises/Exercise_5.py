#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:49:56 2020

Title: Exercise 5

@author: Oliver Reed
"""

# Imitating a fair dice roll.

import random

def dice_roll(n=6):
    num = random.randint(1,n)
    return (num)


for n in range(100):
    dice_roll()
    
    
# Compressing a text

import zlib
import random
import string

def random_string(N):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(N)])

text = """
Welcome, dear Rosencrantz and Guildenstern!
Moreover that we much did long to see you,
The need we have to use you did provoke
Our hasty sending. Something have you heard
Of Hamlet's transformation; so call it,
Sith nor the exterior nor the inward man
Resembles that it was. What it should be,
More than his father's death, that thus hath put him
So much from the understanding of himself,
I cannot dream of: I entreat you both,
That, being of so young days brought up with him,
And sith so neighbour'd to his youth and havior,
That you vouchsafe your rest here in our court
Some little time: so by your companies
To draw him on to pleasures, and to gather,
So much as from occasion you may glean,
Whether aught, to us unknown, afflicts him thus,
That, open'd, lies within our remedy."""


e_text = text * 100
f_text = random_string(78500)

# Convert Python string to bytes and check type
text_bytes = f_text.encode("utf-8")
print(type(text_bytes))

# Get number of bytes used to store string
print("Number of bytes for uncompressed string:", len(text_bytes))

# Compress string and get number of byes used for compressed string
text_comp = zlib.compress(text_bytes)
print("Number of bytes for compressed string:", len(text_comp))

# Display the compression efficiency
print("Compression efficiency: ", len(text_bytes)/len(text_comp))

# Decompress the string
text_decomp = zlib.decompress(text_comp)

# Check that original and decompressed string are the same (more on aseret)
if f_text != text_decomp.decode("utf-8"):
    print("Problem: original and decompressed string differ.")






