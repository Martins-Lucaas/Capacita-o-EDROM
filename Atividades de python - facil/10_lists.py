def process_commands(commands):
    my_list = []
    output = []

    for command in commands:
        if command[0] == "insert":
            i, e = map(int, command[1:])
            my_list.insert(i, e)
        elif command[0] == "print":
            output.append(my_list.copy())
        elif command[0] == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            my_list.append(e)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()

    return output

if __name__ == "__main__":
    n = int(input())
    commands = [input().split() for _ in range(n)]

    result = process_commands(commands)

    for output_list in result:
        print(output_list)