#include <iostream>
#include "include/zstd_client.h"

extern "C" {
#include "zstd.h" 
}

//-----------Estimate Compression Buffer---------------
size_t ZSTDclient::est_compressed_size(size_t source_size)
{
	return ZSTD_compressBound(source_size)+2*1024*1024;
}

//-----------ZSTD COMPRESSION------------
bool ZSTDclient::compress(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size)
{
	//Setting Compression Level:
	int level = 1, ret = 0;

	//---Time measure begins---
	timer.start();

	//Compress
	ret = ZSTD_compress((void* const)destination, destination_size, (void* const)source, source_size, level);
	if(ret != 0){
		std::cout << "Error in ZSTD Compression, @ compress2()!" << std::endl;
		return false;
	}

	//---Time measure ends---
	timer.stop();

	return true;
}

//-----------ZSTD DECOMPRESSION------------
bool ZSTDclient::decompress(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size)
{
	int ret = 0;

	//Allocate destination buffer
	destination = malloc(destination_size);
	if(nullptr == destination){
		std::cout << "Error in ZSTD Decompression, @ malloc()!" << std::endl;
		return false;
	}

	//---Time measure begins---
	timer.start();

	//Decompress
	ret = ZSTD_decompress((void* const)destination, destination_size, (void* const)source, source_size);
	if(ret != 0){
		std::cout << "Error in ZLIB Decompression, @ uncompress2()!" << std::endl;
		free(destination);
		destination = nullptr;
		return false;
	}

	//---Time measure ends---
	timer.stop();

	return true;
}
