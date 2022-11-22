# Python Tech Challenge

## Description
The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000.

## Setup

> This project supports Python 3.7+

* Clone this repo.
* Go to the created folder.
* Start coding.

## Basic Example
```python
from DataCapture.DataCapture import DataCapture


def main():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.less(4))
    print(stats.between(3, 6))
    print(stats.greater(4))


if __name__ == "__main__":
    main()
```


## Testing

Run the following command: `python -m unittest /PATH/TO/PythonChallenge/tests/test_data_capture.py`