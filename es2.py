if __name__ == '__main__':
    print("input string:")
    buffer = input()
    ret = buffer[0]+buffer[1]+buffer[-2]+buffer[-1]
    print(ret)