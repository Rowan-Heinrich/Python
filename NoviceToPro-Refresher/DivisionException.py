while True:
    try:
        x = int(input('enter the first number: '))
        y = int(input('enter the second number: '))
        z=1/0
        print(x/y)
    except Exception as e:
        print('Something went wrong: ', e)
        print('please try again')
    else:
        break
    finally:
        print('cleaning up...')
        del x,y,z
