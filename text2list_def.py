


def text2list():
    input_text = "5 10 3 4 7"
    text2list = input_text.split()
    print(text2list)
    return text2list
    average_list = sum(text2list) / len(text2list)
    print(average_list)
    return average_list
if __name__ == "__main__":
    text2list()
