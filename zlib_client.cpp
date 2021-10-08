#include <iostream>
#include "include/zlib_client.h"

extern "C" {
#include "zlib.h"
}


//-----------Estimate Compression Buffer---------------
size_t ZLIBclient::est_compressed_size(size_t source_size)
{
	return compressBound(source_size)+2*1024*1024;
}

//-----------ZLIB COMPRESSION------------
bool ZLIBclient::compress(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size)
{
	//Setting Compression Level:
	int level = 9, ret = 0;

	//---Time measure begins---
	timer.start();

	//Compress
	ret = compress2((Bytef*)destination, &destination_size, (const Bytef*)source, source_size, level);
	if(ret != 0) {
		std::cout << "Error in ZLIB Compression, @ compress2()!" << std::endl;
		return false;
	}

	//---Time measure ends---
	timer.stop();

	return true;
}

//-----------ZLIB DECOMPRESSION------------
bool ZLIBclient::decompress(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size)
{
	int ret = 0;

	//Allocate destination buffer
	destination = malloc(destination_size);
	if(nullptr == destination){
		std::cout << "Error in ZLIB Decompression, @ malloc()!" << std::endl;
		return false;
	}

	//---Time measure begins---
	timer.start();

	//Decompress
	ret = uncompress2((Bytef*)destination, &destination_size, (const Bytef*)source, &source_size);
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
