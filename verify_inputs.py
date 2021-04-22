
class Verify:

    def __init__(self):

        self.verify_inputs = 0
    
    #no use yet
    def verify_inputs(self, v):
        value = v + 1
        verify_options = list(range(1, value))
        print(verify_options)
        return verify_options