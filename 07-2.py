graph = dict()
line = input()
while line != '':
    steps = line.split(' ')
    if steps[7] not in graph:
        graph[steps[7]] = {steps[1]}
    else:
        graph[steps[7]] |= {steps[1]}
    line = input()

s = set()
for t in graph:
    s |= graph[t]

alphabet = set([chr(t) for t in range(ord('A'), ord('Z')+1)])
s = alphabet - set(graph.keys())
job_queue = set(s)
time = 0
worker_jobs = list(job_queue)
workers = [ord(x) - 4 for x in worker_jobs]
while len(workers) != 5:
    workers.append(worker_jobs.append(None))
job_queue = set()
done = set()
while len(done) < len(alphabet):
    t = min([t for t in workers if t is not None])
    time += t
    print("Workers: ", workers)
    print("Jobs: ", worker_jobs)
    print("Done: ", done)
    print("Queue: ", job_queue)
    for i in range(len(workers)):
        if workers[i] is not None:
            workers[i] -= t
            if workers[i] == 0:
                done |= {worker_jobs[i]}
    for key in graph:
        if graph[key] <= done:
            job_queue |= {key}

    job_queue -= done | set(worker_jobs)
    for i in range(len(workers)):
        if workers[i] == 0 or workers[i] is None:
            if len(job_queue) > 0:
                job = min(job_queue)
                if job not in worker_jobs:
                    workers[i] = ord(job) - 4
                    worker_jobs[i] = job
                job_queue -= {job}
            elif len(job_queue) == 0:
                workers[i] = None
                worker_jobs[i] = None
print(time)
