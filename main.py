import sys
import os.path

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

  

