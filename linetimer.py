import timeit
import time

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()
        self.start_process = time.process_time()   ## added to calculate process-time

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start) * 1000.0
        print(self.name + ' Code block Total time: ' + str(self.took) + ' ms')
        self.processtook = (time.process_time() - self.start_process) * 1000.0
        print(self.name + ' Code block Process time: ' + str(self.processtook) + ' ms')
        print(f'\x1b[6;30;42m {self.name} API Response time: {self.took - self.processtook} ms \x1b[0m')

