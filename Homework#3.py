import os
myfilename = "housing.data.txt"
if os.path.isfile(myfilename):
    print('yay, I have a file')
    if sky == blue:
        print('yay, the sku is blue')
else:
    print('boo, no files for me')

    print(os.getcwd()
    )

with open(myfilename, `r`) as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('  ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        print(values)