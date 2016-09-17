#!/usr/bin/python
import sys
import os
def timeadder(strt,num):
    """func: time addr
        usage : 
            add time in seconds on a time string with format (hh:mm:ss)
        param:
          (string) @strt = the time string
          (float ) @num  = the number of seconds to add
        example:
            timeaddr("10:05:10,5",10.5)
    """
    timelist = strt.split(":")
    hour = timelist[0]
    minute = int(timelist[1])
    second = float(timelist[2].replace(",","."))
    if second + num >= 60:
        minute += 1
        second = num - (60 - second)
    else:
        second += num
    return ":".join([str(hour),str(minute),str(second).replace(".",",")])

def pathspliter(path):
    pathsplit = path.split(os.sep)
    newpath = os.sep.join(pathsplit[0:len(pathsplit)-1])
    return newpath


def makesubtitle(src,des,num):
    linenum = 0
    for line in src:
        word = line.strip()
        linenum += 1
        if "-->" in word :
            timelist = word.split("-->")
            start = timelist[0]
            end = timelist[1]
            start = timeadder(start,num)
            end = timeadder(end,num)
            des.write("-->".join([start,end])+"\n")
        else:
            des.write(word+"\n")

def errorUsage(errstr):
    usage = """ 
                Python Subtitle Adder
                Usage : sub-add [filename] [time to add]
            """
    error = "Error : "+errstr
    return error+usage

if len(sys.argv) < 3:
    print errorUsage("argumen yang di masukan tidak mencukupi, minimal 2 argumen")
    sys.exit(1)

filename = sys.argv[1]
num = float(sys.argv[2])
fopen = open(filename)
folder = pathspliter(filename)
newsub = open(folder+os.sep+filename+".srt","w+r")

makesubtitle(fopen,newsub,num)

newsub.seek(0)
print newsub.read()
fopen.flush()
fopen.close()
newsub.close()
print "done adding ", num, "seconds to ", filename, " !"    

