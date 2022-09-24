# # # import logging
# # # import threading
# # # import time
# # #
# # # def thread_function(name):
# # #     logging.info("Thread %s: starting", name)
# # #     time.sleep(subreddits)
# # #     logging.info("Thread %s: finishing", name)
# # #
# # # if __name__ == "__main__":
# # #     format = "%(asctime)s: %(message)s"
# # #     logging.basicConfig(format=format, level=logging.INFO,
# # #                         datefmt="%H:%M:%S")
# # #
# # #     logging.info("Main    : before creating thread")
# # #     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
# # #     logging.info("Main    : before running thread")
# # #     x.start()
# # #     logging.info("Main    : wait for the thread to finish")
# # #     x.join()
# # #     logging.info("Main    : all done")
# #
# # import logging
# # import threading
# # import time
# #
# # def thread_function(name):
# #     logging.info("Thread %s: starting", name)
# #     time.sleep(subreddits)
# #     logging.info("Thread %s: finishing", name)
# #
# # if __name__ == "__main__":
# #     format = "%(asctime)s: %(message)s"
# #     logging.basicConfig(format=format, level=logging.INFO,
# #                         datefmt="%H:%M:%S")
# #
# #     threads = list()
# #     for index in range(3):
# #         logging.info("Main    : create and start thread %d.", index)
# #         x = threading.Thread(target=thread_function, args=(index,))
# #         threads.append(x)
# #         x.start()
# #
# #     for index, thread in enumerate(threads):
# #         logging.info("Main    : before joining thread %d.", index)
# #         thread.join()
# #         logging.info("Main    : thread %d done", index)
#
#
# # SuperFastPython.com
# # example of a deadlock caused by a thread waiting on itself
# from threading import Thread
# from threading import Lock
#
#
# # task to be executed in a new thread
# def task(lock):
#     print('Thread acquiring lock...')
#     with lock:
#         print('Thread acquiring lock again...')
#         with lock:
#             # will never get here
#             pass
#
#
# # create the mutex lock
# lock = Lock()
# # create and configure the new thread
# thread = Thread(target=task, args=(lock,))
# # start the new thread
# thread.start()
# # wait for threads to exit...
# thread.join()


