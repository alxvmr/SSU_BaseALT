import emoji

def calc(expr):
    return eval(expr)


def show_answer(expr):
    print(emoji.emojize(":backhand_index_pointing_down: Answer is :backhand_index_pointing_down:", language='en'))
    print(calc(expr))
