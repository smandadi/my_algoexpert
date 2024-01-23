#!/usr/bin/env python3

# You recently started freelance software development and have been offered a variety of job opportunities.
# Each job has a deadline, meaning there is no value in completing the work after the deadline. Additionally,
# each job has an associated payment representing the profit for completing that job. Given this information,
# write a function that returns the maximum profit that can be obtained in a 7-day period.

# Each job will take 1 full day to complete, and the deadline will be given as the number of days left to complete
# the job. For example, if a job has a deadline of 1, then it can only be completed if it is the first job worked on.
# If a job has a deadline of 2, then it could be started on the first or second day.

# Note: There is no requirement to complete all of the jobs. Only one job can be worked on at a time,
# meaning that in some scenarios it will be impossible to complete them all.


def optimalFreelancing(jobs):
    totalPayment = 0
    tDays = 7

    while tDays > 0:
        tMax = 0
        idRemove = None

        for idx, data in enumerate(jobs):
            if data["deadline"] >= tDays and data["payment"] > tMax:
                tMax = data["payment"]
                idRemove = idx

        if tMax != 0:
            del jobs[idRemove]
            totalPayment += tMax
        tDays -= 1

    return totalPayment


if __name__ == "__main__":
    jobs = [{"deadline": 1, "payment": 1}, {"deadline": 2, "payment": 2}, {"deadline": 2, "payment": 1}]
    assert optimalFreelancing(jobs) == 3