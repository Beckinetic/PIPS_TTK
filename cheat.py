
def cheat(number = "1.2P.1"):
    if number == "1.2P.1":
        answer = """
        import pandas as pd # generally you would put all import statements at the top
                            # of the script - enables, e.g., easy installation of all 
                            # relevant packages
        
        another_array = np.zeros((2, 4, 6))
        
        # valid solution #1 - indexes the single element
        print(another_array[-1, 0, 2])
        
        # valid solution #2 - subsets the full dimension
        print(another_array[:, 0, :])
        print(another_array[:, :, 2])
        print(another_array[-1, :, :])
        
        # Generally, remember that Python (in contrast to R) 
        #     - is zero-indexed (indices go from 0 to (n-1))
        #     - negative indices "invert" the access instead of deselection
        #     - you need to indicate fully indexed dimensions with a colon
        """
        print(answer)
    elif number == "1.2P.2":
        answer = """
        another_array = np.zeros((2, 4, 6))
        new_array = another_array.copy() 
        # alternatively: new_array = np.copy(another_array)
        new_array[1, 2, 2] = 1
        print(f"another: '{another_array[1, 2, 2]}' vs. new: '{new_array[1, 2, 2]}'")
        
        # In Python, when using =, we only assign a reference to an object in memory,
        # so both new_array and another_array are pointing to the same memory
        # allocation, namely, the one created by np.zeros(). To make a true copy, you
        # can use the .copy() method or np.copy().
        """
        print(answer)
