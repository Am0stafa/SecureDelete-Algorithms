# SecureDelete-Algorithms

This is a collection of secure delete algorithms that can be used to overwrite data in a way that makes it difficult or impossible to recover. The algorithms included in this collection are:

- [Zero-fill](#1-zero-fill)
- [DoD 5220.22-M](#2-dod-522022-m)
- [Random data](#3-random-data)

## 1) Zero-fill

The zero-fill algorithm overwrites the data with zeros, making it difficult to recover. This method involves overwriting the data with a single pass of zeros. While it's the fastest method, it may not be the most secure, as some advanced data recovery techniques might still recover parts of the original data.

## 2) DoD 5220.22-M

The DoD 5220.22-M algorithm overwrites the data with a specific pattern of values, making it very difficult to recover. This method involves three passes:

1. Overwrite with a fixed value (e.g., all zeros or all ones).
2. Overwrite with the complement of the fixed value used in Pass 1 (e.g., all ones or all zeros).
3. Overwrite with random data and verify the final overwrite.

This method is more secure than the zero-fill method, but it's also slower and requires more resources.

## 3) Random data

The random data algorithm overwrites the data with random values, making it more difficult to recover. This method involves overwriting the data with random bytes. While it's the most secure method, it's also the slowest, as it requires generating random bytes and writing them to the file.

## Which algorithm is more secure?
The most secure algorithm is the random data algorithm, as it overwrites the data with completely random values. However, this method is also the slowest and requires more resources. The DoD 5220.22-M algorithm is also very secure and is a good compromise between security and speed. The zero-fill algorithm is the fastest, but it may not be as secure as the other methods.



## How data is deleted on a hard disk

When a file is deleted on a hard disk, the operating system marks the space occupied by the file as available for use. However, the data is not actually erased from the disk until it is overwritten by new data. This means that it's possible to recover deleted files using specialized data recovery software.
<br>
Secure delete algorithms work by overwriting the data with new data, making it more difficult or impossible to recover. On a hard disk, this involves overwriting the data with new values multiple times. The number of times the data is overwritten depends on the algorithm used. The DoD 5220.22-M algorithm, for example, overwrites the data three times.

<br>
It's important to note that secure delete algorithms are not foolproof and may not be able to completely erase all traces of the original data. Advanced data recovery techniques may still be able to recover some or all of the original data. However, using a secure delete algorithm can make it much more difficult to recover the data and can provide an additional layer of security.

<br>

Data is not deleted its just overwritten

## Why is it not useful to use on an SSD?
Solid-state drives (SSDs) use a different technology than hard disk drives (HDDs) to store data. SSDs use flash memory, which has a limited number of write cycles. Overwriting data on an SSD can cause unnecessary wear on the flash memory and reduce the lifespan of the drive. Additionally, SSDs use wear-leveling algorithms that can make it difficult to securely delete data. For these reasons, it's generally not recommended to use secure delete algorithms on SSDs.




### Usage

To use these algorithms, you can either implement them in your own code or use a tool that already implements them. Some examples of tools that use these algorithms are:

- [Secure File Deletion Tool](https://github.com/username/secure-delete-tool)
- [Eraser](https://eraser.heidi.ie/)

### Contributing

Contributions to this collection are welcome! If you have a secure delete algorithm that you'd like to add, please submit a pull request.


