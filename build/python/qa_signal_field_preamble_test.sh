#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/mattias/Desktop/gr-satcom_gmu/python
export PATH=/home/mattias/Desktop/gr-satcom_gmu/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/mattias/Desktop/gr-satcom_gmu/build/swig:$PYTHONPATH
/usr/bin/python2 /home/mattias/Desktop/gr-satcom_gmu/python/qa_signal_field_preamble.py 
