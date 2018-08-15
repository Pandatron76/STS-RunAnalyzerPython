def campfire_visited(run_set):
    return campfire_rested(run_set) + campfire_upgraded(run_set)


def campfire_rested(run_set):
    return sum(run.campfire_rested for run in run_set)


def campfire_upgraded(run_set):
    return sum(run.campfire_upgraded for run in run_set)