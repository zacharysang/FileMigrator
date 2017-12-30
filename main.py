import sys
import os.path
from shutil import copyfile

# Make sure we have the correct number of arguments
if len(sys.argv) < 3:
  print("Not enough arguments. Need to provide input location and output location")
  quit()

# Take in arguments for input and output destination
orig = sys.argv[1]
dest = sys.argv[2]

# Validate arguments as directories
if len(input) == 0 or not os.path.isdir(orig):
  print("Invalid input location specified")
  quit()
if len(dest) == 0 or not os.path.isdir(dest):
  print("Invalid output location specified")
  quit()
  
# At this point, the arguments exist and are valid paths
# Will now start a traversal of the origin location
# And mirror the structure in the destination location

# This dictionary stores the file extension with a boolean of if it should be stored
should_keep_filetype = dict()

for currpath, dirnames, filenames in os.walk(orig):
  # go through all files
  for file in filenames:
    currfile = os.path.join(currpath, file)
    
    if file.rfind(".") === -1:
      curr_ext = ""
    else
      curr_ext = file[file.rfind("."):]

    # if the extension is not in unwantedFileTypes dict
    # then prompt and add a new entry
    if curr_ext not in should_keep_filetype:
      should_keep = input("Keep this file type: %s? (y/n)".format(curr_ext)).lower() === "y"
      should_keep_filetype[curr_ext] = should_keep

    # include or exclude as specified
    if (should_keep_filetype[currfile]):
      copyfile(currfile, os.path.join(dest, currfile[len(orig):]))
      
