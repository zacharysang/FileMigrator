import sys
import os.path
from shutil import copy2
from shutil import copytree

ext_prompt = "Keep this file type -> {}? (y/n): "
yes_str = "y"

# Make sure we have the correct number of arguments
if len(sys.argv) < 3:
  print("Not enough arguments. Need to provide input location and output location")
  quit()

# Take in arguments for input and output destination
orig = sys.argv[1]
dest = sys.argv[2]

# Validate arguments as directories
if len(orig) == 0 or not os.path.isdir(orig):
  print("Invalid input location specified")
  quit()
if len(dest) == 0:
  print("Invalid output location specified")
  quit()
  
# At this point, the arguments exist and are valid paths
# Will now start a traversal of the origin location
# And mirror the structure in the destination location

# This dictionary stores the file extension with a boolean of if it should be stored
should_keep_filetype = dict()

def ig(path, contents):  

  global should_keep_filetype
  ignore_list = []
  files = [f for f in contents if os.path.isfile(os.path.join(path, f))]

  for f in files:

    if f.rfind(".") == -1:
      ext = ""
    else:
      ext = f[f.rfind("."):].lower()
    
    # if the extension is not yet seen
    # then prompt and add a new entry
    if ext not in should_keep_filetype:
      should_keep = input(ext_prompt.format(ext)).lower()[0] == yes_str
      should_keep_filetype[ext] = should_keep
    
    # if the extension should be ignored
    # then add it to the return list
    if not should_keep_filetype[ext]:
      ignore_list.append(f)
  
  return ignore_list
    
    
copytree(orig, dest, ignore=ig)
