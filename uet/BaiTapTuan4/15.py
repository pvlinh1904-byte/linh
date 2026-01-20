con = int(input())
chan = int(input())
cho = (chan - 2 * con) / 2
ga = con - cho
if ga >= 0 and cho >= 0 and cho == int(cho) and ga == int(ga):
    print(int(ga), int(cho))
else:
    print("invalid")