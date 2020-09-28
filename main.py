from pyzeebe import ZeebeWorker


zeebe_worker = ZeebeWorker()


if __name__ == '__main__':
    zeebe_worker.work()