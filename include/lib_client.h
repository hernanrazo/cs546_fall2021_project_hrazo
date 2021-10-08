#include <iostream>
#include "time_counter.h"
#include "data_structure.h"

typedef void*& SOURCE_TYPE;
typedef void*& DESTINATION_TYPE;

class LibClient
{
	public:

		LibClient() = default; //Default Ctor
		~LibClient() = default; //Default Dtor

		//Store uncompressed data
		bool store_uncompressed_data(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size) {
			std::memcpy((char*)destination + Metadata::meta_size, source, source_size);
			return true;
		}

		//Restore uncompressed data
		bool restore_uncompressed_data(SOURCE_TYPE source, size_t source_size, DESTINATION_TYPE destination, size_t &destination_size) {
			destination = std::malloc(destination_size);
			if(destination == nullptr) {
				std::cout << "Can't restore uncompressed data from source" << std::endl;
				return false;
			}
			timer.start();
			std::memcpy(destination, (char*)source, destination_size);
			timer.stop();
			return true;
		}

		//Get execution time in milliseconds
		double time_elapsed_msec()
		{
			return timer.get_duration_msec();
		}

		virtual size_t est_compressed_size(size_t) = 0;
		virtual bool compress(SOURCE_TYPE, size_t, DESTINATION_TYPE, size_t&) = 0;
		virtual bool decompress(SOURCE_TYPE, size_t, DESTINATION_TYPE, size_t&) = 0;

	protected:
		TimeCounter timer;
};
