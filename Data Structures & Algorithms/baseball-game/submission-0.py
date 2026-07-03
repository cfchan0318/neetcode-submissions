class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for op in operations:
            if op == "C":
                points.pop()
            elif op == "D":
                points.append(int(points[-1])*2)
            elif op == "+":
                points.append(int(points[-1]) + int(points[-2]))
            else:
                points.append(int(op))
        return sum(points)