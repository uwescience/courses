import struct as s

# Write N copies of each integer 0..M
# in a packed binary format as an 8-byte long long
def genfile(fn, N,M):
  f = file(fn, "w")
  for i in range(M):
    chunk = s.pack("q"*N, *([i]*N))
    f.write(chunk)

genfile("200mb.dat", 262144, 100)
#genfile("5gb.dat", 8388608, 80)

