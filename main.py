from multiprocessing import Process, Value
from scirpt_sia.EstudianteSia import EstudianteSia


def get_all(dnis, actual_iteration, length):
    for dni in dnis:
        try:
            e = EstudianteSia(dni)
            for i in range(len(e.ha)):
                if e.ha[i].programa != '2542':
                    continue
                acad = open('academic_history.csv', 'a+')
                acad.write(str(e.ha[i]).replace('\t', ','))
                acad.flush()
                schd = open('schedule.csv', 'a+')
                for assign in e.schedule[i]:
                    schd.write(e.dni + ', ' +
                               str(assign).replace(' - ', ',')[1:] + '\n')
                    schd.flush()
                table = open('table_creds.csv', 'a+')
                table.write(dni + ', ')
                aux_write = ''
                for dato in e.table_resume[i]:
                    aux_write += dato + ', '
                aux_write += '$end$'
                table.write(aux_write.replace(', $end$', '\n'))
        except Exception as ex:
            print('Error at dni: ' + str(dni) + '\t', ex)
            blacklist = open('black_list.txt', 'a+')
            blacklist.write(str(dni) + '\n')
            blacklist.flush()
        actual_iteration.value += 1
        print(actual_iteration.value, '/', length)


def main(threads):
    threads = int(threads)
    input_file = open('dnis.txt', 'r')
    dnis = []
    [dnis.append([]) for i in range(threads)]
    it = 0
    for single_dni in input_file.readlines():
        dnis[it % threads].append(single_dni.replace('\n', ''))
        it += 1
    input_file.close()
    counter = Value('i', 0)
    th = []
    for i in range(threads):
        tread = Process(target=get_all, args=(dnis[i], counter, it))
        th.append(tread)
        tread.start()
    [tread.join() for t in th]


if __name__ == '__main__':
    main(100)
