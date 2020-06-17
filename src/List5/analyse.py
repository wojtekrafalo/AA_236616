from copy import copy


def is_legal_config(config):
    first = config[0]
    for c in config:
        if c is not first:
            return False
    return True


def concat_new_history(all_history, new_history):
    all_arr = all_history.split("\n")
    new_arr = new_history.split("\n")
    to_add_arr = []

    for n in new_arr:
        if not all_arr.__contains__(n):
            to_add_arr.append(n)

    for to_a in to_add_arr:
        all_arr.append(to_a)
    for i in range(0, len(all_arr)):
        all_arr[i] += '\n'
    return ''.join(all_arr)


def make_move(config, all_history, history, move=None, first=None):
    leng = len(config)

    made_move = False or (move is None)
    if move is not None:
        if move == 0:
            if config[0] == config[leng - 1]:
                if config[0] == leng:
                    config[0] = 1
                else:
                    config[0] = (config[0] + 1) % (leng + 1)
                history += "-> 0" + str(config)
                made_move = True
        else:
            if config[move] is not config[move-1]:
                config[move] = config[move - 1]
                history += "->" + str(move) + str(config)
                made_move = True
    if not made_move:
        return ""

    if is_legal_config(config):
        return history + "\n"
        # return ""

    copy_config = copy(config)
    new_history = make_move(copy_config, all_history, history, 0)
    all_history = concat_new_history(all_history, new_history)
    for i in range(1, leng):
        copy_config = copy(config)
        new_history = make_move(copy_config, all_history, history, i)
        all_history = concat_new_history(all_history, new_history)
    return all_history + "\n"


def analyse(n):
    config = generate_configs(n)
    ways = ""

    for c in config:
        ways = ways + make_move(c, "", str(c), None, True)
    return ways


def generate_configs(n):
    configs = []
    for i in range(1, n+1):
        configs.append([i])

    for i in range(1, n):
        new_list = []
        for c in configs:
            for j in range(1, n+1):
                new_con = copy(c)
                new_con.append(j)
                new_list.append(new_con)
        configs = new_list
    return configs
