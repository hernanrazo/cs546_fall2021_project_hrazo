#ifndef LZOCLIENT_H
#define LZOCLIENT_H

#include "lib_client.h"

class LZOclient: public LibClient
{
	public:
		size_t est_compressed_size(size_t) override;
		bool compress(SOURCE_TYPE, size_t, DESTINATION_TYPE , size_t&) override;
		bool decompress(SOURCE_TYPE, size_t, DESTINATION_TYPE, size_t&) override;
};
#endif
