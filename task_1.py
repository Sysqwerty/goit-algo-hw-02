from queue import Queue
import time

request_queue = Queue()
is_here = True


def generate_request():
    user_query: str = input("\nEnter a query (or press 'Enter' to exit): ")
    if not user_query:
        global is_here
        is_here = False
    else:
        request_queue.put(user_query)
        print(f"Queue entity has been added: {user_query}")
        print(f"Queue: {', '.join(request_queue.queue)}")


def process_request():
    if not request_queue.empty():
        print("Start query processing...")
        for _ in range(request_queue.qsize()):
            query = request_queue.get()
            print(f"Processing query: {query}")
            time.sleep(0.5)

    print("Queue is empty.")


if __name__ == '__main__':
    while is_here:
        generate_request()
    process_request()
