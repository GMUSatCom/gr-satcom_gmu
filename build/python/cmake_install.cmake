# Install script for directory: /home/mattias/Desktop/gr-satcom_gmu/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/satcom_gmu" TYPE FILE FILES
    "/home/mattias/Desktop/gr-satcom_gmu/python/__init__.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/utils.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/signal_field_preamble.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/tagged_sequence_repeater.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/short_field_preamble.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/short_field_preamble.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/preamble_combiner.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/wifi_scrambler.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/data_formatter.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/data_formatter.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/wifi_interleaver.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/conv_coder.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/debug_sink.py"
    "/home/mattias/Desktop/gr-satcom_gmu/python/OFDM_params.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/satcom_gmu" TYPE FILE FILES
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/__init__.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/utils.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/signal_field_preamble.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/tagged_sequence_repeater.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/short_field_preamble.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/short_field_preamble.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/preamble_combiner.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/wifi_scrambler.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/data_formatter.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/data_formatter.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/wifi_interleaver.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/conv_coder.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/debug_sink.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/OFDM_params.pyc"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/__init__.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/utils.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/signal_field_preamble.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/tagged_sequence_repeater.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/short_field_preamble.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/short_field_preamble.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/preamble_combiner.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/wifi_scrambler.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/data_formatter.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/data_formatter.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/wifi_interleaver.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/conv_coder.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/debug_sink.pyo"
    "/home/mattias/Desktop/gr-satcom_gmu/build/python/OFDM_params.pyo"
    )
endif()

