# Complete the solve function below.
def solve(s):
    name_list = list(s.split(' '))
    name_list = [s.capitalize() for s in name_list]
    res = " ".join(name_list)
    return(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
