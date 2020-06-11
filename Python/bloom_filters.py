# bloom filters are lightweight version of a hash table. Efficient Insertions and Lookup
# More space efficient than hash table, but this comes at the cost of having "false positives" for entry lookup. 

"""
Bloom filters used when you want a data structure that allows for fast lookups and insertions or you care about how much
space the data structure uses. You do not care if the data structure sometimes indicates an item is present when in fact
it is not. 

"""
import pyhash

#List of bits : 0 or 1
bit_vector = [0] * 20

#Non cryptographic hash functions(Murmur and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

#Calculate the output of FNV and Murmur hash functions
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1

bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

print(bit_vector) # will see values 1 at the indices that the vector is present 

fnv_bulb = fnv("Bulbasaur") % 20
murmur_bulb = murmur("Bulbasaur") % 20

print(bit_vector[fnv_bulb])
print(bit_vector[murmur_bulb]) # both will be 0 as haven't changed  