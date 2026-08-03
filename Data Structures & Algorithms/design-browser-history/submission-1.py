class PageNode:
    def __init__(self, page, prev = None, next = None):
        self.val = page
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = PageNode('')
        self.tail = PageNode('')
        homePage = PageNode(homepage, self.head, self.tail)
        self.head.next = homePage
        self.tail.prev = homePage

        self.curr = homePage
        
    def visit(self, url: str) -> None:
        visitPage = PageNode(url, self.curr, self.tail)
        self.tail.prev = visitPage
        self.curr.next = visitPage
        self.curr = visitPage

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr != self.head:
            self.curr = self.curr.prev
            steps -= 1

        # If we reached the dummy head, stop at the first real page
        if self.curr == self.head:
            self.curr = self.head.next

        return self.curr.val


    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr != self.tail:
            self.curr = self.curr.next
            steps -= 1

        # If we reached the dummy tail, stop at the last real page
        if self.curr == self.tail:
            self.curr = self.tail.prev
        
        return self.curr.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)