# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def miniSeq(src, tar):
    res = 0
    cur_idx_tar = 0
    while cur_idx_tar < len(tar):
        last_idx_tar = cur_idx_tar

        for j in range(len(src)):
            if src[j] == tar[cur_idx_tar]:
                cur_idx_tar += 1

        if last_idx_tar != cur_idx_tar:
            res += 1
        elif last_idx_tar == cur_idx_tar:
            return -1

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Test cases
    print(miniSeq("abc", "abcbc"))  # Output: 2
    print(miniSeq("abc", "acdbc"))  # Output: -1
    print(miniSeq("xyz", "xzyxz"))  # Output: 3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
