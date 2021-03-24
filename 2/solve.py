with open("input", "r") as inp:
    puzzle = inp.readlines()

def partA():
    valid = 0

    for line in puzzle:
        policy, pw = line.split(":")
        pw = pw[1:-1]

        policy_l, policy_h = policy.split("-")
        policy_l = int(policy_l)

        policy_h, policy_c = policy_h.split(" ")
        policy_h = int(policy_h)
        
        c_count = pw.count(policy_c)

        if c_count in range(policy_l, policy_h+1):
            valid += 1

    print(valid)

def partB():
    valid = 0

    for line in puzzle:
        policy, pw = line.split(":")
        pw = pw[1:-1]

        policy_l, policy_h = policy.split("-")
        policy_l = int(policy_l)

        policy_h, policy_c = policy_h.split(" ")
        policy_h = int(policy_h)
        
        c_l = pw[policy_l - 1]
        c_h = pw[policy_h - 1]

        if not (c_l == c_h) and ((c_l == policy_c) or (c_h == policy_c)):
            valid += 1

    print(valid)

partB()
