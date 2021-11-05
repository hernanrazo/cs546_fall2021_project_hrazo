#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include "include/time_counter.h"
#include "include/csvfile.h"
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

/*
 * Compress and decompress each file using each compression library.
 * Write resulting information to a csv file. This includes:
 * 1) the file path
 * 2) file size 
 * 3) name of the library used
 * 4) compression/decompression label
 * 5) time taken to compress in seconds (if applicable)
 * 6) time taken to decompress in seconds (if applicable)
 * 7) compression ratio (if applicable)
 */

int main(int argc, char *argv[])
{
	if (argc < 2) {
		std::cout << "No directory argument given" << std::endl;
		std::cout << "Usage: ./main <directory with data files>" << std::endl;
		return(-1);
	}

	std::string dir_path = argv[1];

	ZLIBclient zlib;
	LZOclient lzo;
	ZSTDclient zstd;
	TimeCounter timer;

	FILE *fptr;
	long begin = 0;
	long end = 0;
	size_t source_size = 0;
	size_t destination_size = 0;
	void* source;
	void* destination;

	// file stream for final csv
	csvfile csv("data.csv");

	// traverse files in dir_path
	if (std::filesystem::exists(dir_path) && std::filesystem::is_directory(dir_path)) {
		try {
			for(const auto& entry : std::filesystem::recursive_directory_iterator(dir_path)) {
				if (std::filesystem::is_regular_file(entry.status())) {

					fptr = fopen(entry.path().c_str(), "rb");

					if (!fptr) {
						std::cout << "Could not open file" << std::endl;
						exit(1);
					}

					std::cout << "Currently on file: " << entry.path().c_str() << std::endl;

					// get size of current file in bytes
					fseek(fptr, 0L, SEEK_END);
					source_size = ftell(fptr);
					fseek(fptr, 0L, SEEK_SET);

					// malloc buffers for zlib
					destination_size = zlib.est_compressed_size(source_size);
					source = std::malloc(source_size);
					destination = std::malloc(destination_size);

					// read file pointer to the source buffer
					fread(source, source_size, 1, fptr);

					// zlib compress
					timer.start();
					zlib.compress(source, source_size, destination, destination_size);
					timer.stop();
					csv << entry.path().c_str()
						<< source_size
						<< "zlib"
						<< "compression"
						<< timer.get_duration_sec()
						<< 0
						<< 0
						<< endrow;

					// zlib decompress
					timer.start();
					zlib.decompress(destination, destination_size, source, source_size);
					timer.stop();
					csv << entry.path().c_str()
						<< source_size
						<< "zlib"
						<< "decompression"
						<< 0
						<< timer.get_duration_sec()
						<< source_size / destination_size
						<< endrow;

					free(source);
					free(destination);


					// malloc buffers for lzo
					destination_size = lzo.est_compressed_size(source_size);
					source = std::malloc(source_size);
					destination = std::malloc(destination_size);

					// read file pointer to the source buffer
					fread(source, source_size, 1, fptr);

					// lzo compress
					timer.start();
					lzo.compress(source, source_size, destination, destination_size);
					timer.stop();
					csv << entry.path().c_str()
						<< source_size
						<< "lzo"
						<< "compression"
						<< timer.get_duration_sec()
						<< 0
						<< 0
						<< endrow;

					// lzo decompress
					timer.start();
					lzo.decompress(destination, destination_size, source, source_size);
					timer.stop();
					csv << entry.path().c_str()
						<< source_size
						<< "lzo"
						<< "decompression"
						<< 0
						<< timer.get_duration_sec()
						<< source_size / destination_size
						<< endrow;
					
					free(source);
					free(destination);
					

					// malloc buffers for zstd
					destination_size = zstd.est_compressed_size(source_size);
					source = std::malloc(source_size);
					destination = std::malloc(destination_size);

					// read file pointer to the source buffer
					fread(source, source_size, 1, fptr);

					// zstd compress
					timer.start();
					zstd.compress(source, source_size, destination, destination_size);
					timer.stop();
					csv << entry.path().c_str()
						<< source_size
						<< "zstd"
						<< "compression"
						<< timer.get_duration_sec()
						<< 0
						<< 0
						<< endrow;

					// zstd decompress
					timer.start();
					zstd.decompress(destination, destination_size, source, source_size);
					timer.stop();
					csv << entry.path().c_str()
						<< source_size
						<< "zstd"
						<< "decompression"
						<< 0
						<< timer.get_duration_sec()
						<< source_size / destination_size
						<< endrow;
					
					free(source);
					free(destination);
					fclose(fptr);
				}
			}
		} catch(std::filesystem::filesystem_error const& ex){}
	}
	std::cout << "Data collection complete" << std::endl;
	return(0);
}
