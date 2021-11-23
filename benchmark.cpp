#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "mpi.h"

#include "include/zlib_client.h"
#include "include/lzo_client.h"
#include "include/zstd_client.h"

extern "C" {
#include "lzo/lzo1x.h"
#include "lzo/lzoconf.h"
#include "lzo/lzodefs.h"
#include "zlib.h"
#include "zstd.h"
}

/* Benchmark test for each compression library on a varying amount of processes using MPI.
 * Use this to test each file system. Specify using the output-dir argument. 
 */

int main(int argc, char **argv) {

	int rank, nprocs;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);

	if(argc != 4) {
		std::cout << "USAGE: mpirun -n [nprocs] ./benchmark [compression-method] [input.txt] [output-dir]" << std::endl;
		std::cout << "compression-method: One of LZO, ZSTD, ZLIB, or NONE" << std::endl;
		std::cout << "input.txt: Path to the input file to store and compress." << std::endl;
		std::cout << "output-dir: Path to the directory to store the set of outputs.\n" << std::endl;
		exit(1);
	}
	
	size_t input_size = 0;
	size_t total_input_file_size = 0;
	size_t output_size = 0;
	void *input_buffer;
	void *output_buffer;

	FILE *input_file = fopen(argv[2], "rb");
	FILE *output_file = fopen(argv[3], "w");

	// get the input file's size
	fseek(input_file, 0L, SEEK_END);
	total_input_file_size = ftell(input_file);
	fseek(input_file, 0L, SEEK_SET);

	// Load a portion of the file into memory
	input_size = total_input_file_size / nprocs;
	input_buffer = std::malloc(input_size);
	fseek(input_file, input_size, SEEK_SET);
	fread(input_buffer, input_size, 1, input_file);
	
	// Compress the data (if applicable)
	if(argv[2] == "ZLIB") {
		ZLIBclient zlib;
		output_size = zlib.est_compressed_size(input_size);
		output_buffer = std::malloc(output_size);
		zlib.compress(input_buffer, input_size, output_buffer, output_size);
	}

	else if(argv[2] == "LZO") {
		LZOclient lzo;
		size_t output_size = lzo.est_compressed_size(input_size);
		void *output_buffer = std::malloc(output_size);
		lzo.compress(input_buffer, input_size, output_buffer, output_size);
	}
	else if(argv[2] == "ZSTD") {
		ZSTDclient zstd;
		size_t output_size = zstd.est_compressed_size(input_size);
		void *output_buffer = std::malloc(output_size);
		zstd.compress(input_buffer, input_size, output_buffer, output_size);
	}
	else if(argv[2] == "NONE") {
		// do nothing
	}

	// write the compressed data
	fwrite(output_buffer, output_size, 1, output_file);
	
	fclose(input_file);
	fclose(output_file);
	MPI_Finalize();
	return 0;
}
