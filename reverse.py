''' Reverses a string using recursion '''
def reverse_string(old_str, new_str=""):
    '''Does the thing'''
    if old_str != "":
        new_str += old_str[-1]
        old_str = old_str[0:-1]
        return reverse_string(old_str, new_str)
    return new_str
if __name__ == "__main__":
    print(reverse_string("Hello, world!"))
