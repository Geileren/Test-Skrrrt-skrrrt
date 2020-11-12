class Timetable():
    def __init__(self, table):
        self.table = table

    def check_time(self, time):
        return self.table[time]

    def reserve_time(self, time):
        self.table.update({time: 1})

    def free_time(self, time):
        self.table.update({time: 0})

    def get_table(self):
        return self.table

    def get_table_interval(self, min, max): #kan forbedres ved at fungere med tidsinterval frem for index
        q = list(self.table.items())
        return q[min:max]


class Reservation():
    def __init__(self, table, time, name):
        self.table = table
        if self.table.check_time(time) == 0:
            self.time = time
            self.table.reserve_time(self.time)
        else:
            print("That time is already reserved")
        self.name = name

    def get_name(self):
        return self.name


    def reschedule(self, time):
        if self.table.check_time(time) == 0:
            self.table.free_time(self.time)
            self.time = time
            self.table.reserve_time(self.time)
            self.table.reserve_time(self.time)
        else:
            print("That time is already reserved")

def gen_table(interval, start_time, end_time):
    table = {}
    h = int(start_time[0:start_time.find(":")])
    m = int(start_time[start_time.find(":") + 1:len(start_time)])
    while True:
        if h < 10:
            if m < 10:
                table.update({f"0{h}:0{m}": 0})
            else:
                table.update({f"0{h}:{m}": 0})
        else:
            if m < 10:
                table.update({f"{h}:0{m}": 0})
            else:
                table.update({f"{h}:{m}": 0})

        m += interval
        if m >= 60:
            m -= 60
            h += 1
        if h == int(end_time[0:end_time.find(":")]) and m > int(end_time[end_time.find(":") + 1:len(end_time)]):
            return table


print(gen_table(15, "08:00", "09:30"))
AGC = Timetable(gen_table(15, "08:00", "09:30"))

print(AGC.check_time("08:00"))
AGC.reserve_time("08:00")
print(AGC.check_time("08:00"))

time1 = Reservation(AGC, "08:30", "Lone")
time2 = Reservation(AGC, "08:30", "Dorthe")
print(time2.get_name())


time1.reschedule("09:15")
print(AGC.check_time("09:15"), AGC.check_time("08:30"))
