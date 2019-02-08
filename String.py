#this will find and read the values in a document and print there values as '0', '12.5', etc. and 
# the type of values as string 
import os
myfilename = 'housing.data.txt'

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('  ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        print(values)

print(type(myfilename))

# next step is to convert strings ot intiger 

#Singularity - it is an alternative to a Docker. According to various 
#sources it used by academic community. They are called "containers for 
#scientific research".
#Basically, Docker have a problem with security issues. In Docker 
#superuser have a privilege, but others can access others users data. 
#Singularity uses, for instance, the limited usage to root. Which means 
#that only the root user can run the container. Singularity is the first 
#choice in academic circles when trying to run HPC workloads related to 
#AI.
