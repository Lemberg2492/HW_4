class AnalogRange:
    def __init__(self, start, stop=None, step=1):
        self.__start = start - 1
        self.__stop = stop
        self.__limit = start - 1
        self.__step = step
        self.__count = -1

    def __next__(self):
        if self.__stop != None and self.__step == 1:
            self.__limit = self.__stop - 1

        elif self.__step >= 2:
            self.__limit = self.__stop
            if self.__start < self.__limit-2:
                self.__start += self.__step
                return self.__start-self.__step+1

        elif self.__stop == None:
            self.__limit = self.__start
            if self.__count < self.__limit:
                self.__count += 1
                return self.__count

        if self.__start < self.__limit and self.__step == 1:
                self.__start += self.__step
                return self.__start

        else:
            raise StopIteration

    def __iter__(self):
        return self

print('Analog Range:')
[print(i, end=' ') for i in AnalogRange(20)]

print('\nReal Range:')
[print(i, end=' ') for i in range(20)]
