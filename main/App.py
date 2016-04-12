import logging

__author__ = 'ehongka'


def main():
    """main function"""
    print("start")
    logging.basicConfig(level=logging.DEBUG)
    logging.info("logging is working")
    print("end")

if __name__ == "__main__":
    main()

