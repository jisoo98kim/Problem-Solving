# Link: https://www.acmicpc.net/source/38385387

if __name__ == '__main__':
    fir, sec = map(int, input().split(' ')) # To receive the user input 

    # Compare two values
    if fir > sec:
        print('>')

    elif fir < sec:
        print('<') 

    else:
        print('==')
