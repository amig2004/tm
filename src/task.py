import datetime

class Task:
    def __init__(self, task: str):
        self.task = task 
        self.addDate = datetime.datetime.now()
        
        self.doneDate = None
        self.status = False

    def switchState(self):
        """Switch task status"""
        self.status = not self.status

        # switch date value
        if self.doneDate is None:
            # add current date
            self.doneDate = datetime.datetime.now()
        else:
            self.doneDate = None

    def renderTask(self):
        """Print current task result"""
        parsedStatus = "Done" if self.status is True else "Not Done"

        print(self.addDate)
        print(self.task)
        print()
        if self.status:
            print(f'STATUS: {parsedStatus} | Ended: {self.doneDate}')
        else:
            print(f"STATUS: {parsedStatus}")

    def __repr__(self):
        return f"{self.task}|{self.addDate}|{self.status}|{self.doneDate}"


    def __str__(self):
        return self.renderTask()
        
if __name__ =='__main__':
    tt = Task("Testing, testing")
    tt.renderTask()
    print(tt.__repr__())
    tt.switchState()
    print()
    tt.renderTask()