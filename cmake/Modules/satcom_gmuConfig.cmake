INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SATCOM_GMU satcom_gmu)

FIND_PATH(
    SATCOM_GMU_INCLUDE_DIRS
    NAMES satcom_gmu/api.h
    HINTS $ENV{SATCOM_GMU_DIR}/include
        ${PC_SATCOM_GMU_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SATCOM_GMU_LIBRARIES
    NAMES gnuradio-satcom_gmu
    HINTS $ENV{SATCOM_GMU_DIR}/lib
        ${PC_SATCOM_GMU_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SATCOM_GMU DEFAULT_MSG SATCOM_GMU_LIBRARIES SATCOM_GMU_INCLUDE_DIRS)
MARK_AS_ADVANCED(SATCOM_GMU_LIBRARIES SATCOM_GMU_INCLUDE_DIRS)

