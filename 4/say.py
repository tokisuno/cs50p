import sys
import cowsay

# pyright doesn't like cow, so ignore pyright error notices for it
if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])
