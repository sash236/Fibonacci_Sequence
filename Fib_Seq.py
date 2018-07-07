"""
This code was written to help Data Science students 
One can terminate the code by entering "exit"
Python 3.6.5
"""
import sys

# This function takes the length of the Fibonacci Sequence from user
def get_FS_length():
# While loop ensures a valid entry from the user
# and takes user input of "quit" to exit out
  while True:
    try:
      # Checking if the user entered an integer
      value = input('What is the length of the ' +
         ' Fibonacci Sequence needs to be displayed? ' +
         ' Please limit it to 20:\n ')
      if (value.casefold() in ["exit", "quit", "q"] )  :
        print ('OK - I am quiting')
        break

      FS_length = int(value)  
      if FS_length < 1:
        print("Value needs to be " + 
          "larger than 0 ")
        continue
      elif FS_length > 20:
        print ("Please enter a number less than 20!")    
        continue

    except ValueError:
      # User entered non-integer value hence asking for another entry
      print ("Please enter an integer!")
      continue
    else:   
      # Checking if the entry is a positive value
      return(FS_length)

      
def gen_FS(length):
  seq = []
  
  for n in range(length):
    if n == 0:
      seq.append(0)
    elif n == 1:
      seq.append(1)
    else:
      seq.append(seq[n-1] + seq[n-2])
  
#  print(seq)
  return(seq)

      
def print_to_screen(FS_seq):
  for val in FS_seq:
    print(val)
  
  
def main():
  length = get_FS_length()
  if (length is not None):
    seq = gen_FS(length)
    print("\nHere is the Python generated Fibonacci Sequence:")
    print_to_screen(seq)
  else:
    sys.exit()
  
main()	  