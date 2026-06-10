def test():
    print("Function called")
    return False
resource_ok = test()
if resource_ok == True:
    print("True")
elif resource_ok == False:
    print("False")