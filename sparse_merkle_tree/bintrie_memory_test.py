import new_bintrie as t1
import new_bintrie_optimized as t2
import new_bintrie_hex as t3
import time
import binascii
import psutil
import os
import sys

def print_mem():
    print("#" * 64)
    pid = os.getpid()
    current_process = psutil.Process(pid)
    mem_usage = current_process.memory_info()[0] / 2.**20
    print(f"Current memory KB : {mem_usage: 9.3f} KB")
    print("#" * 64)

keys = [t1.sha3(bytes([i // 256, i % 256])) for i in range(10000)]

print_mem()

if sys.argv[1] == "1":
    d = t1.EphemDB()
    r = t1.new_tree(d)
    a = time.time()
    for k in keys[:10000]:
        r = t1.update(d, r, k, k)
    print("Naive bintree time to update: %.4f" % (time.time() - a))
    print("Root: %s" % binascii.hexlify(r))
    print("Writes: %d, reads: %d" % (d.writes, d.reads))
elif sys.argv[1] == "2":
    d = t2.EphemDB()
    r = t2.new_tree(d)
    a = time.time()
    for k in keys[:10000]:
        r = t2.update(d, r, k, k)
    print("DB-optimized bintree time to update: %.4f" % (time.time() - a))
    print("Root: %s" % binascii.hexlify(r))
    print("Writes: %d, reads: %d" % (d.writes, d.reads))
elif sys.argv[1] == "3":
    d = t3.EphemDB()
    r = t3.new_tree(d)
    a = time.time()
    for k in keys[:10000]:
        r = t3.update(d, r, k, k)
    print("DB-hex bintree time to update: %.4f" % (time.time() - a))
    print("Root: %s" % binascii.hexlify(r))
    print("Writes: %d, reads: %d" % (d.writes, d.reads))

print_mem()
