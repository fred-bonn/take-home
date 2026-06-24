def get_injured(party, threshold):
    injured = []
    for i, member in enumerate(party):
            if 0 < member < threshold:
                  injured.append(i)
    return injured