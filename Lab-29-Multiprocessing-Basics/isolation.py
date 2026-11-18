import multiprocessing

data = []

def add():
    data.append(1)
    print("Child sees:", data)

if __name__ == '__main__':
    p = multiprocessing.Process(target=add)
    p.start()
    p.join()
    print("Parent sees:", data)
