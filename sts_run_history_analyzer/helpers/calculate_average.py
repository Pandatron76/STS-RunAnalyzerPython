# try/excepts are in place to account for users who have unlocked but not played a character


def score(run_set):
    total_score = 0
    no_score_count = 0
    for run in run_set:
        if isinstance(None, type(run.score)) is False:
            total_score += run.score
        elif isinstance(None, type(run.score)) is True:
            no_score_count += 1
        else:
            print("Issue with calculating average score")

    while True:
        try:
            return total_score / (len(run_set) - no_score_count)
        except ZeroDivisionError:
            return 0


def floor_reached(run_set):
    while True:
        try:
            return sum(run.floor_reached for run in run_set) / len(run_set)
        except ZeroDivisionError:
            return 0
