fname=input('Enter the file name:mbox.txt')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:',fname)
    quit()
