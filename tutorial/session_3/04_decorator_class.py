class RepeatLogger:
    def __init__(self , n):
        self.n = n
        self.counter = 0
    
    def __call__(self, func):
        def run_call(*args, **kwargs):
            for i in range(self.n):
                # self.counter = self.counter + 1
                self.counter += 1
                print(f'[{self.counter}]')
                func(*args, **kwargs)
        return run_call

@RepeatLogger(2)
def test(text):
    print(f'{text}')

test('start class...')
        