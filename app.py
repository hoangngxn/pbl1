def read_input_file(filename):
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        p = list(map(int, f.readline().split()))
        d = list(map(int, f.readline().split()))
    return n, p, d


def schedule_jobs(n, p, d):
    jobs = sorted(enumerate(zip(p, d), start=1), key=lambda x: x[1][1])  # Sort by deadline
    schedule = []
    current_time = 0
    completed_jobs = 0
    
    for job in jobs:
        job_id, (processing_time, deadline) = job
        if current_time + processing_time <= deadline:  # Can complete before the deadline
            schedule.append(job_id)
            current_time += processing_time
            completed_jobs += 1
    
    return completed_jobs, schedule


def write_output_file(filename, completed_jobs, schedule):
    with open(filename, "w") as f:
        f.write(f"{completed_jobs}\n")
        f.write(" ".join(map(str, schedule)) + "\n")


if __name__ == "__main__":
    input_file = "LICHD.INP"
    output_file = "LICHD.OUT"
    
    n, p, d = read_input_file(input_file)
    completed_jobs, schedule = schedule_jobs(n, p, d)
    write_output_file(output_file, completed_jobs, schedule)
