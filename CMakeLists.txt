cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(project)

set(INSTALL_DIR $ENV{INSTALL_DIR})
set(INCLUDE_DIRS "-L${INSTALL_DIR}/lib/")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${INCLUDE_DIRS}")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${INCLUDE_DIRS}")

include_directories(include)
include_directories(${CMAKE_BINARY_DIR}/lib/zlib-1.2.11)
include_directories(${CMAKE_BINARY_DIR}/lib/lzo-2.10)
include_directories(${CMAKE_BINARY_DIR}/lib/zstd-1.0.0)

add_executable(main main.cpp
	zlib_client.cpp
	lzo_client.cpp
	zstd_client.cpp
	include/time_counter.h
	include/csvfile.h
	include/zlib_client.h
	include/lzo_client.h
	include/zstd_client.h)

add_executable(pred pred.cpp
	zlib_client.cpp
	lzo_client.cpp
	zstd_client.cpp
	include/time_counter.h
	include/csvfile.h
	include/zlib_client.h
	include/lzo_client.h
	include/zstd_client.h)


target_link_libraries(pred
	/home/hernanrazo/project/lib/zlib-1.2.11/libz.so
	/home/hernanrazo/project/lib/lzo-2.10/src/.libs/liblzo2.so
	/home/hernanrazo/project/lib/zstd-1.0.0/lib/libzstd.so)

target_link_libraries(main
	/home/hernanrazo/project/lib/zlib-1.2.11/libz.so
	/home/hernanrazo/project/lib/lzo-2.10/src/.libs/liblzo2.so
	/home/hernanrazo/project/lib/zstd-1.0.0/lib/libzstd.so)

set_property(TARGET main pred PROPERTY CXX_STANDARD 17)
