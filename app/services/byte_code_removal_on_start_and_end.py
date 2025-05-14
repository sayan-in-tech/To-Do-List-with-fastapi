def deleteByteCode():
    import os
    import sys

    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the .pyc file
    pyc_file = os.path.join(script_dir, '__pycache__', 'byte_code_removal_on_start_and_end.cpython-39.pyc')

    # Check if the .pyc file exists and delete it
    if os.path.exists(pyc_file):
        os.remove(pyc_file)
    else:
        # If the .pyc file does not exist, print an error message
        print(f"Error: {pyc_file} does not exist.")
