import os
import sys
import psutil


def view():
   for process in psutil.process_iter():
        name = process.name()
        pid = process.pid
        memory = process.memory_percent()
        procesor = process.cpu_percent()
        print("Process name =", name, ",", "Process ID =", pid, "Used memory =", memory, ",", "Processor used =", procesor)
        try:
            print(f'Current directory: {process.cwd()} \n')
        except psutil.AccessDenied:
            print('(You do not have access to this process) \n')


def suspend(pid):
    try:
        process = psutil.Process(int(pid))
        process.suspend()
    except Exception as e:
        print(f"error: {e.__str__()} ")
    else:
        print("The process was suspended")


def resume(pid):
    try:
        process = psutil.Process(int(pid))
        process.resume()
    except Exception as e:
        print(f"error: {e.__str__()}")
    else:
        print("The process was resumed")


def kill(pid):
    try:
        os.kill(int(pid), 9)
    except Exception as e:
        print(f"error: {e.__str__()}")
    else:
        print("The process was killed")


def run(path, *args):
    try:
        parameters = ''
        for p in args[0]:
            parameters = parameters + " " + p
        os.popen(path + " " + parameters)
    except Exception as e:
        print(f"error: {e.__str__()}")
    else:
        print("The process has started")


if __name__ == '__main__':
    if sys.argv[1] == "run":
        list_args = [item for index, item in enumerate(sys.argv) if index >= 3]
        run(sys.argv[2], list_args)
    elif sys.argv[1] == "kill":
        kill(sys.argv[2])
    elif sys.argv[1] == "suspend":
        suspend(sys.argv[2])
    elif sys.argv[1] == "resume":
        resume(sys.argv[2])
    elif sys.argv[1] == "view":
        view()
    else:
        print("Introduce a valid command")
