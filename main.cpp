#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <torch/script.h>
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


int main(int argc, char *argv[]) {

	if (argc < 2) {
		std::cout << "No directory argument given" << std::endl;
		std::cout << "Usage: ./main <directory with data files>" << std::endl;
		return(-1);
	}

	std::string dir_path = argv[1];
	
	ZLIBclient zlib;
	LZOclient lzo;
	ZSTDclient zstd;
	
	long begin = 0;
	long end = 0;
	size_t source_size = 0;
	void* source;

	size_t destination_size = 0;
	void* destination;

	// file stream for final csv
	std::ofstream outfile ("data.csv");

	// traverse files in dataset
	if (std::filesystem::exists(dir_path) && std::filesystem::is_directory(dir_path)) {
		try {
			for(const auto& entry : std::filesystem::recursive_directory_iterator(dir_path)) {
				if (std::filesystem::is_regular_file(entry.status())) {
				
					// get needed values for each compression/decompression
					std::ifstream stream (entry.path().c_str());

					if (!stream) {
						std::cout << "Could not open file stream" << std::endl;
						continue;
					}

					std::cout << "Currently on file: " << entry.path().c_str() << std::endl;

					// get source size
					begin = stream.tellg();
					stream.seekg(0, std::ios::end);
					end = stream.tellg();
					source_size = (end - begin);

					// get source buffer
					source = std::malloc(source_size);

					// compress
					zlib.compress(source, source_size, destination, destination_size);
					//lzo.compress(source, source_size, source, source_size);
					//zstd.compress(source, source_size, source, source_size);

					// decompress
					//zlib.decompress(source, source_size, source, source_size);
					//lzo.decompress(source, source_size, source, source_size);
					//zstd.decompress(source, source_size, source, source_size);
					
					stream.close();
					outfile << "test" << std::endl;
				}
			}
		} catch(std::filesystem::filesystem_error const& ex){}
	}
	outfile.close();
	std::cout << "Data collection complete" << std::endl;
	return(0);
}
