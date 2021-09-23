cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(CS546)

find_package(Torch REQUIRED)
set(INSTALL_DIR $ENV{INSTALL_DIR})
set(INCLUDE_DIRS "-L${INSTALL_DIR}/lib/")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS} ${INCLUDE_DIRS}")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${INCLUDE_DIRS}")


include_directories(${CMAKE_BINARY_DIR}/lib/zlib-1.2.11)

add_executable(main main.cpp)
target_link_libraries(main "${TORCH_LIBRARIES}")
set_property(TARGET main PROPERTY CXX_STANDARD 14)
