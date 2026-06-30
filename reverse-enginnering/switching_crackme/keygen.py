from itertools import permutations

def check_id_xor(pass_str):
    rax_2 = int(pass_str[0])
    rax_6 = int(pass_str[len(pass_str) - 1])
    rax_8 = rax_2 ^ rax_6
    return rax_8 if rax_8 >= rax_2 and rax_8 >= rax_6 else -1

def check_id_sum(pass_str, xor_val):
    if xor_val == -1:
        return False
    var_20 = 0
    for i in range(1, len(pass_str) - 1):
        if i % 2 == 1:
            var_20 += int(pass_str[i])
        else:
            var_20 -= int(pass_str[i])
    return var_20 == xor_val

for i in range(5, 10):
    for perm in permutations("1234567890", i):
        pass_str = "".join(perm)
        xor_val = check_id_xor(pass_str)
        if check_id_sum(pass_str, xor_val):
            print("A password was found: ", pass_str)
            break
