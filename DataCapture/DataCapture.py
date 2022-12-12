from dataclasses import dataclass


@dataclass
class Node:
    count: int
    less: int
    greater: int


class Stats:
    def __init__(self, data: dict, length: int) -> None:
        self.__data: dict = data
        self.__length: int = length

    def less(self, number: int) -> int:
        return self.__data[number].less

    def between(self, smaller_number: int, larger_number: int) -> int:
        return (
                self.__length
                - self.__data[smaller_number].less
                - self.__data[larger_number].greater
        )

    def greater(self, number: int) -> int:
        return self.__data[number].greater


class DataCapture:
    def __init__(self) -> None:
        self.data: dict = {}
        self.max_value: int = 0
        self.length: int = 0

    def add(self, number: int) -> None:
        if number > self.max_value:
            self.max_value = number
        # if number not in self.data:
        #     self.data[number] = Node(count=0, less=0, greater=0)
        # self.data[number].count += 1
        try:
            self.data[number].count += 1
        except:
            self.data[number] = Node(count=1, less=0, greater=0)
        self.length += 1

    def build_stats(self) -> Stats:
        accum: int = 0
        for number in range(1, self.max_value + 1):
            if number in self.data:
                self.data[number].less = accum
                accum += self.data[number].count
                self.data[number].greater = self.length - accum

        return Stats(self.data, self.length)
