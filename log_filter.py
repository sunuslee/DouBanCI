#!/usr/bin/env python3.1
import sys
import time
def main():
        fread = open(sys.argv[1])
        fwrite = open(sys.argv[2], "w")
        word_filter = sys.argv[3]
        fwrite.write("Generate Time {0}\n".format(time.ctime()))
        for line in fread.readlines():
                if (word_filter in line) or (("START" or "END")  in line):
                        fwrite.write(line)
        fread.close()
        fwrite.close()
main()
