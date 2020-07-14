from task import Task
import datetime
import os

class Taskbase:
    DEF_BASE_PATH = "~/.tmbase" 

    @staticmethod
    def checkBaseExist():
        result = os.path.isfile(Taskbase.DEF_BASE_PATH)
        return result

    def __init__(self):
        self.tasks = []
        self.saved = False

    def checkTaskList(self):
        """Check if given task list contains only objects of type TASK"""
        for tsk in self.tasks:
            if not isinstance(tsk, Task):
                raise Exception('Taskbase data corrupted')
            else:
                continue
        # if its ok -> return true, else raise exception
        return True

    def checkIndexPresence(self, id: int):
        """Checks if given index vlaue exist in curren self.tasks list"""
        if id < 0:
            return False
        
        if id > len(self.tasks) - 1:
            return False
        else: 
            return True



    def addTask(self, taskvalue: str):
        """Add task to self.tasks"""
        self.tasks.append(Task(taskvalue))
        self.saved = False

    def deleteTask(self, id: int):
        del self.tasks[id]
        self.saved = False

    def switchState(self,id: int):
        self.tasks[id].switchState()
        self.saved = False


    def saveTasksToFile(self):
        dbfile = open(Taskbase.DEF_BASE_PATH, "w+")

        for tsk in self.tasks:
            f.write(tsk.__repr__)

        dbfile.close()

        self.saved = True

    def loadTasksFromFile(self):
        dbfile = open(Taskbase.DEF_BASE_PATH, "r")

        for tsk in self.tasks:
            line = f.read()

            # separate values from given line
            content = line.split("|")

            current = Task(content[0])
            current.addDate = datetime.datetime.strptime(content[1])
            
            # handle status and data parsing
            if content[2] == "False":
                current.status = False
                current.doneDate = None
            else:
                current.status = True
                current.doneDate = datetime.datetime.strptime(content[3])

        # close file
        dbfile.close()


    def printTasks(self):
        if self.tasks:
            for tsk in self.tasks:
                print("---------------------------------")
                tsk.renderTask()
            
            print("---------------------------------")
        else:
            print("No tasks added")

if __name__ == "__main__":
    tb = Taskbase()
    tb.addTask('Costam jedenn')
    tb.addTask('Costam dwa')
    tb.addTask('Costam trzy')

    tb.printTasks()

    tb.switchState(1)

    print('__________________________________________________')
    tb.printTasks()

    tb.saveTasksToFile()