#include <cstring>
#include <string>
#include "enumerations.h"

class Data
{
	public:
		CompressionLibrary lib = CompressionLibrary::DUMMY;
		double comp_time = 0;
		double decomp_time = 0;

		void setLib(int lib_id) {
			lib = static_cast<CompressionLibrary>(lib_id);
		}

		void setLib(CompressionLibrary lib_) {
			lib = lib_;
		}

		void resetTimers() {
			comp_time = 0;
			decomp_time = 0;
		}
};

class Metadata
{
	public:

		const static size_t meta_size = sizeof(bool) + sizeof(size_t);
		bool is_compressed;
		size_t uncomp_size;

		Metadata() {
		}

		//bool Encode(void *uncomp_buf, size_t uncomp_size, void *comp_buf, size_t comp_size, bool is_compressed) {
		void Encode(void *uncomp_buf, size_t uncomp_size, void *comp_buf, size_t comp_size, bool is_compressed) {
			size_t loc = 0;
			std::memcpy(comp_buf, &is_compressed, sizeof(bool));
			loc += sizeof(bool);
			std::memcpy((char*)comp_buf + loc, &uncomp_size, sizeof(size_t));
		}

		void Decode(void *comp_buf) {
			size_t loc = 0;
			std::memcpy(&is_compressed, comp_buf, sizeof(bool));
			loc += sizeof(bool);
			std::memcpy(&uncomp_size, (char*)comp_buf + loc, sizeof(size_t));
		}
};
