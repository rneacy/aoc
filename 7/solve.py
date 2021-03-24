from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    inp = f.read().splitlines()

pairs = {}

for line in inp:
    dependant = line[36]
    requirement = line[5]

    if dependant not in pairs:
        pairs[dependant] = [requirement]
    else:
        pairs[dependant].append(requirement)

    if requirement not in pairs:
        pairs[requirement] = []

def partA():
    steps = ""
    completed = []

    while len(completed) < len(pairs):
        # search for available step
        pending = []
        for pair in pairs:
            # remove completed steps
            for c in completed:
                if c in pairs[pair]:
                    pairs[pair].remove(c)

            if not pairs[pair] and pair not in completed and pair not in pending: # available
                pending.append(pair)

        pending.sort()
        completed.append(pending[0])
        steps += pending[0]

    print(steps)

def partB():
    completed = []

    workercount = 5
    workers = { i:'' for i in range(workercount)}
    worktime = 0

    keylist = list(pairs.keys())
    keylist.sort()
    optimes = { keylist[i]:60+i+1 for i in range(len(keylist)) }

    inprogress = []

    while len(completed) < len(pairs):
        print("Work time: " + str(worktime))
        for worker in workers:
            if not workers[worker]: # worker needs job
                print("Worker " + str(worker) + " needs job.")
                pending = []

                for pair in pairs:
                    for c in completed:
                        if c in pairs[pair]:
                            pairs[pair].remove(c)
                    
                    if not pairs[pair] and pair not in completed and pair not in inprogress and pair not in pending: # available
                        pending.append(pair)

                if pending:
                    pending.sort()
                    workers[worker] = pending[0]
                    inprogress.append(pending[0])
                    print("Worker " + str(worker) + " assigned job " + pending[0])

            if workers[worker]:
                print("Worker " + str(worker) + " is working on job " + workers[worker], end="")
                print(" with " + str(optimes[workers[worker]]) + "s remaining.")
                optimes[workers[worker]] -= 1

                if optimes[workers[worker]] < 1:
                    completed.append(workers[worker])
                    inprogress.remove(workers[worker])
                    print("Worker " + str(worker) + " has finished job " + workers[worker] + " at work time " + str(worktime + 1))
                    workers[worker] = ""

        worktime += 1

        print()

    print("Total work time: " + str(worktime))
    print(completed)
    print(inprogress)

#partA()
partB()