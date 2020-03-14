import os, sys

def initca():
    foldera = 'path/instagram/AvailablePseudos'
    for filenamea in os.listdir(foldera):
        file_patha = os.path.join(foldera, filenamea)
        try:
            if os.path.isfile(file_patha) or os.path.islink(file_patha):
                os.unlink(file_patha)
            elif os.path.isdir(file_patha):
                shutil.rmtree(file_patha)
        except:
            sys.exit(" Error #2. Please report your error to https://github.com/Gumbraise/HXYA/issues with a screenshot of the console")
    print (' Cache Cleared')