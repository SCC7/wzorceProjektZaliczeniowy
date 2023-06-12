import time


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# # Usage example
# import time
#
# # A List of Items
# items = list(range(0, 57))
# l = len(items)
#
# # Initial call to print 0% progress
# # print('test') # działa, nie znika podczas aktualizacji progresu
# printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(0.1)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

def pasek_postepu_instant(dlugosc=50, prefixProcesu='PROCES'):
    points = list(range(0, int(dlugosc)));
    pointsLength = len(points);
    # nazwaProcesu = 'Postęp mielenia ziaren kawy:'
    printProgressBar(0, pointsLength, prefix=prefixProcesu, length=50);
    for i, points in enumerate(points):
        time.sleep(0.01);
        printProgressBar(0 + i, pointsLength, prefix=prefixProcesu, length=50);
    printProgressBar(pointsLength, pointsLength, prefix=prefixProcesu, length=50);
