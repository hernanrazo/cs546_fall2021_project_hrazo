#include <iostream>
#include "include/lzo_client.h"

extern "C" {
#include "lzo/lzo1x.h"
#include "lzo/lzoconf.h"
#include "lzo/lzodefs.h"
}


//-----------Estimate Compression Buffer---------------
size_t LZOclient::est_compressed_size(size_t source_size)
{
	return source_size + source_size / 16 + 64 + 3;
}

//-----------LZO COMPRESSION------------
bool LZOclient::compress(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size)
{
	lzo_voidp work_mem = nullptr;

	//LZO init
	if(lzo_init() != 0){
		std::cout << "Error in LZO Compression, @ lzo_init()!\n" << std::endl;
		return false;
	}

	//Allocate work memory
	work_mem = malloc(LZO1X_1_MEM_COMPRESS);

	//---Time measure begins---
	timer.start();

	//Compress
	if (0 != lzo1x_1_compress((const lzo_bytep)source, (lzo_uint)source_size, (lzo_bytep)destination, &destination_size , work_mem)){
		std::cout << "Error in LZO Compression, @ lzo1x_1_compress()!" << std::endl;
		free(work_mem);
		return false;
	}

	//---Time measure ends---
	timer.stop();

	free(work_mem);
	return true;
}

//-----------LZO DECOMPRESSION------------
bool LZOclient::decompress(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size)
{
	int lzoError = 0;

	//LZO init
	if(lzo_init() != 0){
		std::cout << "Error in LZO Decompression, @ lzo_init()!\n" << std::endl;
		return false;
	}

	//Allocate destination buffer
	destination = malloc(destination_size);
	if(nullptr == destination){
		std::cout << "Error in LZO Decompression, @ malloc()!" << std::endl;
		return false;
	}

	//---Time measure begins---
	timer.start();

	//Decompress
	lzoError = lzo1x_decompress((const lzo_bytep)source, (lzo_uint)source_size, (lzo_bytep)destination, &destination_size, NULL);
	if(0 != lzoError){
		std::cout << "Error in LZO Decompression, @ lzo1x_1_decompress()!" << std::endl;
		free(destination);
		destination = nullptr;
		return false;
	}

	//---Time measure ends---
	timer.stop();

	//Update destination
	return true;
}
