import os
import argparse
import random


argparser = argparse.ArgumentParser(description="Secure file deletion tool")
argparser.add_argument("-f", "--file", help="File to delete")
argparser.add_argument("-d", "--directory", help="Directory to delete")
argparser.add_argument("-n", "--passes", type=int, default=3, help="Number of overwrite passes (default: 3)")
# argparser.add_argument("-m", "--method", default="zero-fill", help="Overwrite method (default: zero-fill)")
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
  for _ in range(2):
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
  for _ in range(2):
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

