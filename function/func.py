from traceback import extract_tb
def func1():
    int('fffffffffffffff')

def run_with_log(func):
    with open('errors.txt','a') as file:
        try:
            func()
        except Exception as e:
            file.write(str(type(e))+'\n '+str(e)+'\n '+str(extract_tb(e.__traceback__)))

run_with_log(func1)
