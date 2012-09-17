from winazurestorage import *
import base64
import sys

def do_blob_tests(account, key):
    '''Expected output:
        Starting blob tests
                create_container: 201
                put_blob: 201
                get_blob: Hello, World!
                delete_container: 202
        Done.
    '''
    print "Starting blob tests"
    if account is None or key is None: blobs = BlobStorage()
    else: blobs = BlobStorage(CLOUD_BLOB_HOST, account, key)
    print "\tcreate_container: %s" % blobs.create_container("testcontainer", True)
    print "\tput_blob: %s" % blobs.put_blob("testcontainer", "testblob.txt", "Hello, World!")
    print "\tget_blob: %s" % blobs.get_blob("testcontainer", "testblob.txt")
    print "\tput_block: %s" % blobs.put_block("testcontainer", "testblob.txt", base64.encodestring('foobar'), 'something')
    print "\tlist_blobs: %s" % [x for x in blobs.list_blobs("testcontainer")]
    #print "\tdelete_container: %d" % blobs.delete_container("testcontainer")
    #print "Done."

def do_table_tests(account, key):
    if account is None or key is None:
        print "Skipping table tests, since no account and key were passed on the command line."
        return
    print "Starting table tests"
    tables = TableStorage(CLOUD_TABLE_HOST, account, key)
    print "\tcreate_table: %d" % tables.create_table("testtable")
    print "\tget_all: %d" % len(tables.get_all("testtable"))
    print "\tdelete_table: %d" % tables.delete_table("testtable")
    print "Done"

def do_queue_tests(account, key):
    print "Starting queue tests"
    if account is None or key is None: queues = QueueStorage()
    else: queues = QueueStorage(CLOUD_QUEUE_HOST, account, key)
    print "\tcreate_queue: %d" % queues.create_queue("testqueue")
    print "\tdelete_queue: %d" % queues.delete_queue("testqueue")
    print "Done"

def run_tests(account, key):
    do_blob_tests(account, key)
    do_table_tests(account, key)
    do_queue_tests(account, key)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        run_tests(sys.argv[1], sys.argv[2])
    else:
        account = raw_input("Enter storage account name: ")
        key = raw_input("Enter primary access key (secret key): ")
        run_tests(account, key)
