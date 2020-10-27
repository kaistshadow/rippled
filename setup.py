from distutils.command.build_ext import build_ext
from distutils.core import setup, Extension
import os
import shutil

def exec_shell_cmd(cmd):
    if os.system(cmd) != 0:
        print("error while executing '%s'" % cmd)
        exit(-1)

def create_ripple():
    exec_shell_cmd("rm -rf build")
    exec_shell_cmd("mkdir build && cd build && cmake .. && make -j 8")


def create_libarchive():
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/libarchive && rm -rf build2")
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/libarchive && mkdir build2 && cd build2 && cmake .. && make -j 4")


def create_soci():
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci && rm -rf build")
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci && mkdir build && cd build && cmake .. && make -j 4")

def create_sqlite3():
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/sqlite3 && rm -rf build")
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/sqlite3 && mkdir build && cd build && cmake .. && make -j 4")

        

if __name__ == '__main__':
    exec_shell_cmd("export BOOST_ROOT=~/boost_1_70_0")
    # create_ripple()
    # create_libarchive()
    # create_sqlite3()
    # create_soci()
    f = open("librippled.txt","r")
    line = f.readline()
    exec_shell_cmd(line)
