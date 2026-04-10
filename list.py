#Solution for https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
the_list = []
for _ in range(N):
        parts = input().split()
        command = parts[0]
        args = parts[1:]

        match command:
            case 'insert':
                the_list.insert(int(args[0]), int(args[1]))
            case 'print':
                print(the_list)
            case 'remove':
                the_list.remove(int(args[0]))
            case 'append':
                the_list.append(int(args[0]))
            case 'sort':
                the_list.sort()
            case 'pop':
                the_list.pop()
            case 'reverse':
                the_list.reverse()
