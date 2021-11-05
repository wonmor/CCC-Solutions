original_num_list = [1, 2]
original_num = 12
hour_count = 0
final_hour_count = 0
initializer = 0
usable_value = []
final_count = 0
minute_count = 0

def startJam():
    for i in range(minute_count + 1):

        global final_num_list
        global usable_value

        if minute_count < 10:
            usable_value.append(0)
            usable_value.append(i)

        elif minute_count >= 10:
            usable_value = [*map(int, str(i))]

        comparison1 = abs(final_num_list[0] - final_num_list[1])
        comparsion2 = abs(final_num_list[1] - usable_value[0])
        comparison3 = abs(usable_value[0] - usable_value[1])

        if comparison1 == comparsion2 == comparison3:
            final_count + 1

    print(final_count)

duration = input()

if int(duration) >= 60:
    hour_count = int(duration / 60)
    minute_count = int(duration % 60)
    minute_count_list = [*map(int, str(minute_count))]
    final_hour_count = original_num + hour_count
    final_num_list = [*map(int, str(final_hour_count))]
    final_num_list.append(minute_count_list[0])
    final_num_list.append(minute_count_list[1])

    startJam()

elif int(duration) < 60:
    final_hour_count = original_num
    final_minute_count = duration

    final_num_list = [*map(int, str(final_hour_count))]

    final_minute_list = [*map(int, str(final_minute_count))]

    final_num_list.append(final_minute_list[0])
    final_num_list.append(final_minute_list[1])

    startJam()