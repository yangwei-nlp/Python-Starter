
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        queue = []
        seen = []
        all_employee = {}
        for person in employees:
            if person.id == id:
                queue.append(person.id)
                seen.append(person.id)
            all_employee[person.id] = [person.id, person.importance, person.subordinates]
            # [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
        importance_sum = 0
        while queue:
            id = queue.pop(0)
            importance_sum += all_employee[id][1]  # 每次弹出的时候加上这个值就可以了！
            for employee_id in all_employee[id][2]:
                if employee_id not in seen:
                    # 注意，这时候千万别加上这个值
                    # importance_sum += all_employee[employee_id][1]
                    seen.append(all_employee[employee_id][0])
                    queue.append(all_employee[employee_id][0])
        return importance_sum


e_1 = Employee(1, 5, [2, 3])
e_2 = Employee(2, 3, [])
e_3 = Employee(3, 3, [])
s = Solution()
print(s.getImportance([e_1, e_2, e_3], 1))