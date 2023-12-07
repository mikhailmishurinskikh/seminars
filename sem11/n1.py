def simple_multiplier(num):
    if not isinstance(num, int): return 'error'
    if num == 1: return 1
    if num < 1: return 'error'
    not_changed_num = num+0
    i = 2
    answer = []
    while num != 1 and i < num ** 0.5 + 1:
        if num % i == 0:
            answer += [i]
            num //= i
        else: i += 1
    if num != 1: answer += [num]
    if len(answer) == 1: answer = answer[0]
    else: answer = tuple(answer)
    return answer
