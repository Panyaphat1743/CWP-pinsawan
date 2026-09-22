import sys

if len(sys.argv) == 1:
    print("none")
else:

    params = sys.argv[1:]
    
    print(f"parameters: {len(params)}")
    
    for param in params:
        print(f"{param}: {len(param)}")