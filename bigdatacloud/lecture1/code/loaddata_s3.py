import os.path
import StringIO
import sys
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import time
import multiprocessing as p

def mkprogress(chunk):
  def progress(sofar,total):
    print "%.1f/%.1f MB of chunk %s transferred (%.1f%%)" % (float(sofar)/2**20,float(total)/2**20,chunk,100*sofar/float(total))
    sys.stdout.flush()
  return progress

def readChunk(fn,offset=0,size=None):
  f = file(fn, "rb")
  if size == None: size = os.path.getsize(fn) - offset
  f.seek(offset)
  chunk = f.read(size)
  f.close()
  return chunk

def connect(keys):
  return S3Connection(**keys)

def reconstruct_mp(mp_info, keys):
  conn = connect(keys)
  bucket = conn.lookup(mp_info[0])
  mp = boto.s3.multipart.MultiPartUpload(bucket)
  mp.key_name = mp_info[1]
  mp.id = mp_info[2]
  return mp

def sendChunk(args):
  fn,offset,size,i,mp,keys = args
  chunk = readChunk(fn,offset,size)
  mp = reconstruct_mp(mp, keys)
  sio = StringIO.StringIO(chunk)
  mp.upload_part_from_file(sio, i+1, cb=mkprogress(i), num_cb=70)

def parallelUpload(bucketname, fn, numChunks, keys):
  conn = connect(keys)
  print "Creating bucket"
  bucket = conn.create_bucket(bucketname)
 
  bucket.delete_key(fn)

  start = time.time()
  mp = bucket.initiate_multipart_upload(fn) #reduced_redundancy=use_rr)

  chunkSize = os.path.getsize(fn) / numChunks
  arglist = [(fn, i*chunkSize, chunkSize, i, (mp.bucket_name, mp.key_name, mp.id), keys) for i in range(numChunks)]

  print "Sending chunks ", chunkSize, numChunks
  
  pool = p.Pool(processes=numChunks)
  pool.map_async(sendChunk, arglist).get(999999)

  mp.complete_upload()
  end = time.time()

  key = bucket.get_key(fn)
  print "Upload successful.  Time to transfer:"
  print ("AWS", os.path.getsize(fn), numChunks, end - start)

if __name__ == '__main__':
  keys = {}
  if len(sys.argv) < 6:
    keys['aws_access_key_id'] = raw_input("Enter AWS access key: ")
    keys['aws_secret_access_key'] = raw_input("Enter AWS secret key: ")
    bucketname = raw_input("Enter bucket name: ")
    fn = raw_input("Enter file name to upload: ")
    N = int(raw_input("Enter number of chunks to upload in parallel: "))
  else:
    keys['aws_access_key_id'] = sys.argv[1]
    keys['aws_secret_access_key'] = sys.argv[2]
    bucketname = sys.argv[3]
    fn = sys.argv[4]
    N = int(sys.argv[5])

  parallelUpload(bucketname, fn, N, keys)
 
