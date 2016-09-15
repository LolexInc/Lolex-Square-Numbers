
import sys,os,subprocess,io,time
sys.path.insert(0,"\\")
try:
    import squarenumber
except(ImportError):
    with open ("squarenumber.py","a") as f: f.write("squarenumbers = 2\noriginsquare = 2")
    subprocess.call("Squarensquare.py",shell = True)
import squarenumber
squarenumbers = squarenumber.squarenumbers
originsquare = squarenumber.originsquare
gone = 0
while True:
    squarenumbers = originsquare*originsquare
    originsquare = originsquare + 1
    print(squarenumbers)
    #time.sleep(0.2)
    gone = gone + 1
    if gone == 1000 or gone>1000:
        os.remove("squarenumber.py")
        with open ("squarenumber.py","a") as f: f.write("squarenumbers = ")
        with open ("squarenumber.py","a") as outf: outf.write(str(squarenumbers))
        with open ("squarenumber.py","a") as f: f.write("\noriginsquare = ")
        with open ("squarenumber.py","a") as outf: outf.write(str(originsquare))
        gone = 0

