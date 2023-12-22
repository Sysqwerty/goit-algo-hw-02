from queue import Queue
import time
import uuid
import signal

request_queue = Queue()
is_running = True


def generate_request():
    request_id = str(uuid.uuid4())  # Генеруємо унікальний ID для заявки
    request_queue.put(request_id)
    print(f"Request {request_id} added to the queue.")
    print(f"Queue: {', '.join(request_queue.queue)}")
    time.sleep(1)


def process_request():
    if not request_queue.empty():
        print("Start processing requests...")
        while not request_queue.empty():
            request_id = request_queue.get()
            print(f"Processing request: {request_id}")
            time.sleep(1)
        print("Queue is empty.\n")
    else:
        print("Queue is empty.\n")


def handle_exit(signum, frame):
    global is_running
    is_running = False
    print("\nExiting the program...")


# Додаємо обробник сигналу преривання для можливості коректного виходу з програми
signal.signal(signal.SIGINT, handle_exit)

if __name__ == '__main__':
    try:
        while is_running:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        pass
    finally:
        print("Program terminated.")
