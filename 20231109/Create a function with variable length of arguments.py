def func1(*args):
    print('列印值')
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)