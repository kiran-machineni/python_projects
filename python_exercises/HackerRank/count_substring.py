def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string)+1):
        if string[i:len(sub_string)+i] == sub_string:
            count += 1
        i += 1
    return count


print(count_substring("ABCDCDC", "CDC"))
