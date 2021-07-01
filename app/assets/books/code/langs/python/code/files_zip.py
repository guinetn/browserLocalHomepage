"""Data Compression.

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

Common data archiving and compression formats are directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile.
"""




# Compressing Files
# The Python standard library enables you to work with different types of compressed files like tar, zip, gzip, bzip2.
# To work with a zip file you can use the zipfile module:
import zipfile 
my_zip = zipfile.ZipFile('zipped_file.zip', mode='r') 
print(file.namelist())

# You can create a zip file from your files like this:
import zipfile 
file=zipfile.ZipFile('files.zip','w') 
file.write('file1.txt') 
file.close()

# You can extract the zip file using extractall() method like this:
import zipfile 
file=zipfile.ZipFile('files.zip','r') 
file.extractall() 
file.close()

# Also, you can append files to existing zip file by using append mode like this:
import zipfile 
file=zipfile.ZipFile('files.zip','a') 
file.write('file2.txt') 
file.close()

# The same coding above is done when dealing with gz or bz files. You need to use gzip module or bz2 module.
import gzip 
import bz2 
gz_file=gzip.GzipFile('files.gz','r') 
bz_file=bz2.BZ2File('fiels.bz2','r')

# Then you can read and write in the same way.
# You can deal with rar files using unrar package. First, install the package
pip install unrar
# Then you can use it the same way.
import unrar.rarfile 
m=unrar.rarfile.RarFile('file.rar') 
m.namelist() 
m.extractall()



# Extracting from Zip files in Python
# import zipfile
from zipfile import ZipFile

# path to the zipfile
file = './Importing files.zip'

# read zipfile and extract contents
with ZipFile (file, 'r') as zip:
    zip.printdir()
    zip.extractall()





import zlib


def test_zlib():
    """zlib."""
    string = b'witch which has which witches wrist watch'
    assert len(string) == 41

    zlib_compressed_string = zlib.compress(string)
    assert len(zlib_compressed_string) == 37

    zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
    assert zlib_decompressed_string == b'witch which has which witches wrist watch'

    assert zlib.crc32(string) == 226805979
