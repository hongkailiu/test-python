import logging
import sys
import pydevd

__author__ = 'ehongka'


def main():
    """main function"""
    print("start")
    logging.basicConfig(level=logging.DEBUG)
    logging.info("logging is working")
    print("end")


if __name__ == "__main__":
    print("111")
    pydevd.settrace('142.133.110.134', port=51234)
    main()
