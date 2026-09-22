import sys

if len(sys.argv) == 1:
    print("none")
else:

    for param in sys.argv[1:]:
        
        if param.endswith("ism"):
            continue
        print(param + "ism")