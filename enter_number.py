# This is a module.

# Return the number (integer or float) input by user with its type.

def EnterNumber(sentence="Enter a number"):
   
   cpt = 0

   while cpt != -1:
      x = input("\n" + sentence + ": ")
      try:
         x = int(x)
         # Only if x is integer:
         cpt = -1
      except:
         cpt = 1

      if cpt == 1:
         try:
            x = float(x)
            # Only if x is float:
            cpt = -1
         except:
            pass

   return x

# Example (executed only if this script is the main):
if __name__ == "__main__":
   sentence = "Enter a number"
   res = EnterNumber(sentence)
   print(f"Your number: {res}", f"Type of your number: {type(res)}", sep="\n")
