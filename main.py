import os
import csv


inputfilepath = 'P:\\Tabletennis\\2023Edgeball\\'
outputfilepath = inputfilepath + 'Highlights\\'

def runbash(command):
    os.system(command)


def crop(start, end, doinput, output):
    dostr = "ffmpeg -i " + doinput + " -ss  " + start + " -to " + end + " -c:v libx265 -crf 26 -preset medium -c:a aac -b:a 128k " + output
    print(dostr)
    runbash(dostr)


def dotrim2(filename):
    path = outputfilepath
    if not os.path.exists(path):
        os.makedirs(path)
    index = 1
    concatstr = ''
    with open(inputfilepath + filename + ".csv", newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            rowlist = row[0].split(',')
            crop(rowlist[0], rowlist[1], inputfilepath + filename + ".MOV", path + filename + "-" + str(index) + ".MOV")
            index += 1
    print(concatstr)


def doread(filename):
    if os.path.isfile(inputfilepath + filename + ".csv"):
        with open(inputfilepath + filename + ".csv", newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                print(row[0])
                if os.path.isfile(inputfilepath + row[0] + ".csv"):
                    dotrim2(row[0])


if __name__ == '__main__':
    fname = input("Enter file name: ")
    doread(fname)

