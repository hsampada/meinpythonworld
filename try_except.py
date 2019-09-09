import sys
try:
    num=input('enter number:')
    print(4/num)
except ZeroDivisionError as E:
    print(E)
    print("number greater than 0")
except ImportError as E:
    print(E)
except NameError as E:
    print (E)
except Exception as E:
    print(E)
else:
    print("im in else")
finally:
    print("executes in every condition")
