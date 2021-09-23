#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "lzo/lzo1x.h"
#include "lzo/lzoconf.h"
#include "lzo/lzodefs.h"
#include "zlib.h"
#include <zstd.h>
#include <torch/script.h>

using namespace std;


#define CHUNK 16384

// function prototypes
void zerr(int ret);
int zlib_compress(FILE *source, FILE *dest, int level);


// report zlib errors
void zerr(int ret) {

    fputs("zpipe: ", stderr);
    switch (ret) {
    case Z_ERRNO:
        if (ferror(stdin))
            fputs("error reading stdin\n", stderr);
        if (ferror(stdout))
            fputs("error writing stdout\n", stderr);
        break;
    case Z_STREAM_ERROR:
        fputs("invalid compression level\n", stderr);
        break;
    case Z_DATA_ERROR:
        fputs("invalid or incomplete deflate data\n", stderr);
        break;
    case Z_MEM_ERROR:
        fputs("out of memory\n", stderr);
        break;
    case Z_VERSION_ERROR:
        fputs("zlib version mismatch!\n", stderr);
    }
}


int zlib_compress(FILE *source, FILE *dest, int level) {
	int ret; // return codes
	int flush; // keep ttrack of current flushing state for deflate()
	unsigned have; // amount of data returned from deflate()
	z_stream strm; // pass info to and from zlib
	unsigned char in[CHUNK]; // input buffer
	unsigned char out[CHUNK]; // output buffer

	// allocate deflate state
	strm.zalloc = Z_NULL;
	strm.zfree = Z_NULL;
	strm.opaque = Z_NULL;

	// check return value of deflateInit() to make sure that it was able to allocate memory for 
	// the internal state. Also check that if argument is valid.
	ret = deflateInit(&strm, level);

	if (ret != Z_OK) {
		return ret;
	}

	// read the input file
	do {
		// grab numberof bytes
		strm.avail_in = fread(in, 1, CHUNK, source);

		// check for errors reading input file
		if (ferror(source)) {
			(void)deflateEnd(&strm);
			return Z_ERRNO;
		}
		// check for end of file and check for last compressable byte
		flush = feof(source) ? Z_FINISH : Z_NO_FLUSH;

		// place pointer to read bytes into next_in
		strm.next_in = in;

		do {
			// run deflate() on input until output buffer not full.
			// finish compression if all of the source has been read.
			strm.avail_out = CHUNK;
			strm.next_out = out;

			// actually compress the file,
			// asserting that the state is not clobbered.
			ret = deflate(&strm, flush);
			assert(ret != Z_STREAM_ERROR);

			// calculate how much output was provided on the last call
			have = CHUNK - strm.avail_out;

			// write data to output file
			if (fwrite(out, 1, have, dest) != have || ferror(dest)) {
				(void)deflateEnd(&strm);
				return Z_ERRNO;
			} 
		} while (strm.avail_out == 0);
		assert(strm.avail_in == 0);
	
	} while (flush != Z_FINISH);
	assert(ret == Z_STREAM_END);

	(void)deflateEnd(&strm);
	return Z_OK; // finished compressing
}



// main function where everything gets implemented
int main(int argc, char **argv) {

	int ret;

    	// do compression if no arguments
    	if (argc == 1) {
		ret = zlib_compress(stdin, stdout, Z_DEFAULT_COMPRESSION);
		if (ret != Z_OK)
	    	zerr(ret);
		return ret;
    	}
    	cout << "done compressing" << endl;
}
