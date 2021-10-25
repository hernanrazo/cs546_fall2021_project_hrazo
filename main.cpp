#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <torch/script.h>
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
 * 3) size of source buffer
 * 4) size of destination buffer
 * 5) time taken to compress/decompress
 * 6) compression/decompression label
 * 7) name of the library used
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
	int file_size = 0;
	size_t buf_size = 0;
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
				
					// open a stream for the current file
					std::ifstream stream;

					if (!stream) {
						std::cout << "Could not open stream" << std::endl;
						exit(1);
					}

					fptr = fopen(entry.path().c_str(), "r");

					if (!fptr) {
						std::cout << "Could not open file" << std::endl;
						exit(1);
					}

					std::cout << "Currently on file: " << entry.path().c_str() << std::endl;

					// get size of current file in bytes
					fseek(fptr, 0L, SEEK_END);
					file_size = ftell(fptr);
					fseek(fptr, 0L, SEEK_SET);

					// malloc buffers
					buf_size = zlib.est_compressed_size(file_size);
					source = std::malloc(buf_size+1);
					destination = std::malloc(buf_size+1);

					// populate source buffer with contents of current file
					fwrite(source, sizeof(source), 1, fptr);
					//std::cout << sizeof(source) << std::endl;

					// zlib compress
					timer.start();
					zlib.compress(source, source_size, destination, destination_size);
					timer.stop();
					csv << entry.path().c_str()
					    << file_size
					    << sizeof(source)
					    << sizeof(destination)
					    << timer.get_duration_msec() 
					    << "compression"
					    << "zlib"
					    << endrow;
					
					// zlib decompress
					timer.start();
					zlib.decompress(source, source_size, destination, destination_size);
					timer.stop();
					csv << entry.path().c_str()
					    << file_size
					    << sizeof(source)
					    << sizeof(destination)
					    << timer.get_duration_msec() 
					    << "decompression"
					    << "zlib"
					    << endrow;
					
					// reset buffer and free memory for next compression library
					buf_size = 0;
					free(source);
					free(destination);

					//close current file when complete
					fclose(fptr);
					stream.close();
				}
			}
		} catch(std::filesystem::filesystem_error const& ex){}
	}
	std::cout << "Data collection complete" << std::endl;
	return(0);
}
