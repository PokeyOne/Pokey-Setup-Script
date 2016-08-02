import sys
import os


def debug(msg: str):
    """
    print out a message with "[DEBUG]" as a prefix
    :param msg: string to print
    :return: void
    """
    print("[DEBUG]" + msg)


def string_from_array(array, suffix=""):
    """
    create a string from an array of strings
    :param suffix: string to append on each string in array
    """
    result = ""
    for char in array:
        result += char + suffix
    return result


def remove_escapes(string):
    """
    removes escapes(e.g. \n and \t) from string given
    :param string: string to remove escapes from
    :return: escaped string
    """
    chars = list(string)
    index = 0
    while index < len(chars):
        if chars[index] == "\\":
            if chars[index+1] == "n":
                chars[index] = "\n"
                chars[index+1] = ""
            elif chars[index+1] == "t":
                chars[index] = "\t"
                chars[index+1] = ""
        index += 1
    new_string = string_from_array(chars)
    return new_string


def run(path: str, workspace: str):
    """
    runs the given PSS file
    :param path: path to Pokey Setup Script file
    :param workspace: path to workspace to setup
    :return: void
    """
    file = open(path, 'r')
    file_content = file.read()
    file.close()
    print("")

    lines = file_content.split("\n")
    lineIndex = 0
    for line in lines:
        words = line.split(" ")
        if len(words) > 0:
            command = words[0]
            if command == "print":
                index = 0
                output = "[Program Output] "
                while index < len(words):
                    if index > 0:
                        output += words[index] + " "
                    index += 1
                print(output)
            elif command == "create":
                path = words[1]
                created_file = open(workspace + path, "w")
                if len(words) > 2 and words[2] == "with":
                    index = 3
                    output = ""
                    while index < len(words):
                        output += words[index] + " "
                        index += 1
                    output = remove_escapes(output)
                    created_file.write(output)
                created_file.close()
            elif command == "createdir":
                path = words[1]
                if not os.path.exists("{0}{1}".format(workspace, path)):
                    os.makedirs("{0}{1}".format(workspace, path))
            elif len(list(string_from_array(words))) > 0:
                print('[ERROR]: UNKNOWN COMMAND! [Line: {0}]: "{1}"'.format(lineIndex, string_from_array(words)))
        lineIndex += 1


if len(sys.argv) > 2:
    run(sys.argv[1], sys.argv[2])
else:
    run("/Volumes/PKYDRV/PSSFiles/defaultWebsite.pss", "/Volumes/PKYDRV/PSSFiles/")
