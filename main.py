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
