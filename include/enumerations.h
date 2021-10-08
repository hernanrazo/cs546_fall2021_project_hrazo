//---------------| USER CHOICES |-----------------

#define NUM_LIBRARIES 3
#define NUM_DATA_TYPES 8

enum class CompressionLibrary //"lib_choice" argument
{
	/* 0     1     2      3     */
	DUMMY, ZLIB, LZO, DYNAMIC //MAKE DYNAMIC THE LAST OPTION DUE TO ITERATORS!!!
};


enum class DataFormat:int{
	//0       1      2     3      4      5     6    7      8      9
	DUMMY, BINARY, MPIIO, HDF5, NETCDF, CSV, JSON, XML, PARQUET, AVRO
};

enum class PathType
{
	NONE, FILE, DIRECTORY
};
