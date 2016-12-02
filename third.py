def step(s, e, count):
    if s == e:
        print "Minimum steps required: ", count

    if s > e:
        s -= 1
        count += 1
        step(s=s, e=e, count=count)

    elif s < e:
        s = s*2
        count = count + 1
        step(s=s, e=e, count=count)


def main():
    test_num = int(input("Enter the number(1-10) of test Cases:"))
    if test_num < 1 or test_num > 10:
		print "Value out of Range"
    for num in range(test_num):
        s = int(input("Enter Starting Point(1-1000): "))
        e = int(input("Enter Destination Point(1-1000): "))
        if s <= 0 or s > 1000 or e <= 0 or e > 1000:
			print "Value out of Range"
			step(s, e,count=0)

if __name__ == '__main__':
    main()
