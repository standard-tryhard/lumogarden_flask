# Import the os module, for the os.walk function
import os
 
def envelope(text_file):
    with open(text_file, 'r') as fin:
        help = [line.strip() for line in fin.readlines()]
        help = [line for line in help if line]
        return help

# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    # garbage, dirName = dirName.split('./')
    print('Found directory: %s' % dirName)
    for fname in fileList:
        name = fname[0:-4]
        open_me = ('{}/{}'.format(dirName, fname))
        # print(open_me) 
        # print(len(['']))
        print(name, envelope(open_me)) if len(envelope(open_me)) > 1 else print('')
        # with open(fname, 'r') as fin:
            # print(fin.readlines())
# print(os.listdir())


