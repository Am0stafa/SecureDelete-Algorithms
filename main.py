import os
import argparse
import random

'''To delete a file or directory first move this script to the directory where the file or directory is located and then run the script with the -f or -d option and the file or directory name as an argument. You can also specify the overwrite method with the -m option. The default method is zero-fill. You can also use dod_5220_22_m or random_data. The script will delete the file or directory and overwrite the data with the specified method.'''

'''There are several secure delete algorithms that can be used to overwrite data in a way that makes it difficult or impossible to recover.'''


argparser = argparse.ArgumentParser(description="Secure file deletion tool")
argparser.add_argument("-f", "--file", help="File to delete")
argparser.add_argument("-d", "--directory", help="Directory to delete")
argparser.add_argument("-m", "--method", default="zero-fill", help="Overwrite method (default: zero-fill) you can also use dod_5220_22_m or random_data")
args = argparser.parse_args()


def zero_fill(file_path):
  """
  Securely delete a file using the single-pass zero-fill method.

  This method involves overwriting the data with a single pass of zeros.
  While it's the fastest method, it may not be the most secure, as some
  advanced data recovery techniques might still recover parts of the
  original data. The function opens the file in binary append mode ("ba+")
  with buffering=0 to prevent any caching of data. It then gets the file's
  length, seeks back to the beginning, and writes zeros over the entire file.
  After the overwrite is complete, the file is deleted

  Args:
    file_path (str): The path to the file to securely delete.

  Raises:
    FileNotFoundError: If the file is not found.
    PermissionError: If there is no permission to delete the file.
  """
  try:
    with open(file_path, "ba+", buffering=0) as f:
      length = f.tell() # Get the file's length in bytes
      f.seek(0)
      f.write(bytearray(length)) # Overwrites the file's content with zeros. b'\x00\x00\x00'
  except FileNotFoundError as e:
    print(f"Error: File not found - {file_path}")
    return
  except PermissionError as e:
    print(f"Error: Permission denied - {file_path}")
    return
  except Exception as e:
    print(f"Error: {e}")
    return

  os.remove(file_path)

def dod_5220_22_m(file_path):
  """
  Securely delete a file using the DoD 5220.22-M 3-pass method.

  This method involves three passes:
  Pass 1: Overwrite with a fixed value (e.g., all zeros or all ones).
  Pass 2: Overwrite with the complement of the fixed value used in Pass 1 (e.g., all ones or all zeros).
  Pass 3: Overwrite with random data and verify the final overwrite.

  Args:
    file_path (str): The path to the file to securely delete.

  Raises:
    FileNotFoundError: If the file is not found.
    PermissionError: If there is no permission to delete the file.
  """

  try:
    with open(file_path, "ba+", buffering=0) as f:
      length = f.tell() # Get the file's length in bytes

      # Pass 1: Overwrite with zeros
      f.seek(0)
      f.write(bytearray(length))

      # Pass 2: Overwrite with ones
      f.seek(0)
      f.write(bytearray([0xFF] * length))

      # Pass 3: Overwrite with random data
      f.seek(0)
      random_data = bytearray(random.getrandbits(8) for _ in range(length)) # Generate random bytes
      f.write(random_data)

      # Verify the final overwrite
      f.seek(0)
      file_data = f.read()
      if file_data != random_data:
        print(f"Error: Verification failed - {file_path}")
        return

  except FileNotFoundError as e:
    print(f"Error: File not found - {file_path}")
    return
  except PermissionError as e:
    print(f"Error: Permission denied - {file_path}")
    return
  except Exception as e:
    print(f"Error: {e}")
    return

  os.remove(file_path)

def random_data(file_path):
  """
  Securely delete a file using the random data method.

  This method involves overwriting the data with random bytes.
  While it's the most secure method, it's also the slowest, as it
  requires generating random bytes and writing them to the file.
  The function opens the file in binary append mode ("ba+")
  with buffering=0 to prevent any caching of data. It then gets the file's
  length, seeks back to the beginning, and writes random bytes over the entire file.
  After the overwrite is complete, the file is deleted

  Args:
    file_path (str): The path to the file to securely delete.

  Raises:
    FileNotFoundError: If the file is not found.
    PermissionError: If there is no permission to delete the file.
  """
  try:
    with open(file_path, "ba+", buffering=0) as f:
      length = f.tell() # Get the file's length in bytes
      f.seek(0)
      random_data = bytearray(random.getrandbits(8) for _ in range(length)) # Generate random bytes
      f.write(random_data)
  except FileNotFoundError as e:
    print(f"Error: File not found - {file_path}")
    return
  except PermissionError as e:
    print(f"Error: Permission denied - {file_path}")
    return
  except Exception as e:
    print(f"Error: {e}")
    return

  os.remove(file_path)

if __name__ == "__main__":
  if args.file:
    if args.method == "zero-fill":
      zero_fill(args.file)
    elif args.method == "dod_5220_22_m":
      dod_5220_22_m(args.file)
    elif args.method == "random_data":
      random_data(args.file)
    else:
      print(f"Error: Invalid method - {args.method}")
  elif args.directory:
    if args.method == "zero-fill":
      for root, dirs, files in os.walk(args.directory):
        for file in files:
          zero_fill(os.path.join(root, file))
    elif args.method == "dod_5220_22_m":
      for root, dirs, files in os.walk(args.directory):
        for file in files:
          dod_5220_22_m(os.path.join(root, file))
    elif args.method == "random_data":
      for root, dirs, files in os.walk(args.directory):
        for file in files:
          random_data(os.path.join(root, file))
    else:
      print(f"Error: Invalid method - {args.method}")
  else:
    print("Error: No file or directory specified")
