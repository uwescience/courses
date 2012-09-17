from winazurestorage import *
import base64
import sys
import os.path
import multiprocessing as mp
import time

def readChunk(fn,offset=0,size=None):
  f = file(fn)
  if size == None: size = os.path.getsize(fn) - offset
  f.seek(offset)
  chunk = f.read(size)
  f.close()
  return chunk

conn = {'conn':None}

def putblock(args):
  print "putting block %s" % (args,)
  account, key, container, fn, offset, size, id = args
  chunk = readChunk(fn, offset, size)
  blobs = BlobStorage(CLOUD_BLOB_HOST, account, key)
  #blobs = conn['conn']
  
  resp = blobs.put_block(container, fn, base64.encodestring(id), chunk)
  print "\tput_block: %s" % resp
  
def listblobs(account, key):
  blobs = BlobStorage(CLOUD_BLOB_HOST, account, key)
  for x in blobs.list_blobs("test"):
    print x

def run_test(account, key, container, fn, numChunks):
  blobs = BlobStorage(CLOUD_BLOB_HOST, account, key)
  conn['conn'] = blobs
  try: 
    print "\tcreate_container: %s" % blobs.create_container(container, True)

    start = time.time()
    chunkSize = os.path.getsize(fn) / numChunks
    pool = mp.Pool(processes=numChunks)
    arglist = [(account, key, container, fn, i*chunkSize, chunkSize, "%s" %i) for i in range(numChunks)]
    pool.map_async(putblock, arglist).get(9999999)
    #putblock((account, key, container, fn, 0, chunkSize, "0"))
  finally:
    end = time.time()
    print "\tdelete_container: %s" % blobs.delete_container(container)
  print "Done."
  print "Upload complete.  Time:"
  print ("Azure", os.path.getsize(fn), numChunks, end - start)

if __name__ == '__main__':
    #listblobs(sys.argv[1], sys.argv[2])
    #sys.exit()
    if len(sys.argv) > 4:
        run_test(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]))
    else:
        account = raw_input("Enter storage account name: ")
        key = raw_input("Enter primary access key (secret key): ")
        container = raw_input("Enter container name (any string): ")
        fn = raw_input("Enter file name to upload: ")
        N = int(raw_input("Enter number of chunks to upload in parallel: "))
        run_test(account, key, container, fn, N)
