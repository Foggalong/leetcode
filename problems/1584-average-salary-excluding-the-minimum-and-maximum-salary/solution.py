class Solution:
    def average(self, salary: List[int]) -> float:
        """
        Takes a list of integers as inputs and returns the average
        value after excluding the maximum and minimum value.
        """

        # guaranteed three salaries, use for initial values
        [min_salary, avg_salary, max_salary] = sorted(salary[0:3]) 
        salary_count   = 1

        # now process fourth salary onwards 
        for employee in salary[3:]:
            if employee < min_salary:
                # add previous minimum to average
                avg_salary += min_salary
                # save new minimum salary
                min_salary = employee
            elif employee > max_salary:
                # add previous maximum to average
                avg_salary += max_salary
                # save new maximum salary
                max_salary = employee
            else:
                # add current salary to average
                avg_salary += employee
            # in any case, added one to average
            salary_count += 1
        
        # to get average, divide running total by count
        return avg_salary/salary_count
