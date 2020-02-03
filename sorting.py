import random


class Sort:

    def __init__(self, count):
        self.count = count

    def lstgen(self, count):
        randlist = []
        while len(randlist) < count:
            r = random.randrange(1, count + 1)
            if r not in randlist:
                randlist.append(r)
        return randlist

    def pusirki(self):
        print('-' * self.count, 'Пузырьковая сортировка', '-' * self.count)
        rnd_list = self.lstgen(self.count)
        cyc = 1
        while cyc == 1:
            cyc = 0
            for i in range(1, len(rnd_list)):
                if rnd_list[-i] < rnd_list[-i-1]:
                    rnd_list[-i], rnd_list[-i-1] = rnd_list[-i-1], rnd_list[-i]
                    cyc = 1
                    print(rnd_list)

    def vibor(self):
        print('-' * self.count, 'Сортировка выбором', '-' * self.count)
        rnd_list = self.lstgen(self.count)
        i = 0
        while i < len(rnd_list) - 1:
            min_num = min(rnd_list[i:])
            for ind in range(0, len(rnd_list)):
                if rnd_list[ind] == min_num:
                    rnd_list[ind], rnd_list[i] = rnd_list[i], rnd_list[ind]
                    break
                ind += 1
            i += 1
            print(rnd_list)


a = Sort(30).pusirki()
b = Sort(30).vibor()




