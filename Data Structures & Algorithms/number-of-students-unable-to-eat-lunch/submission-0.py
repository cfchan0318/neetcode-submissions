class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #take sandwich
        #sandwiches.pop()

        #leave queue
        # del students[0]
        
        #re-enter queue
        #students.append(someone)

        #return number of students undable to eat
        curr_s_round = 1
        while(len(sandwiches) > 0):
            if curr_s_round > len(students):
                break

            if sandwiches[0] == students[0]:
                del sandwiches[0]
                del students[0]
                curr_s_round = 1
            else:
                students.append(students[0])
                del students[0]
                curr_s_round += 1
                
        
        return len(students)
                