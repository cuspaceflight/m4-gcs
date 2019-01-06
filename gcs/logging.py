"""
Logging process
CUSF 2018/19
"""
import os
import threading
import queue

script_dir = os.path.dirname(__file__)


def produce(usb_pipe, gui_exit, q):
    while not gui_exit.is_set():
        if not q.full():
            if usb_pipe.poll(0.1):
                new_packet = usb_pipe.recv()
                q.put(new_packet)


# TODO:
#     - Saves information to log files as the program runs

def run(usb_pipe, gui_exit, log_ready, log_dir):
    """Main loop for logging process

    usb_pipe -- pipe to/from USB process
    gui_exit -- GUI exit signal
    log_dir  -- directory to save log files inside"""
    q = queue.Queue()
    producer = threading.Thread(target=produce, args=(usb_pipe, gui_exit, q))
    producer.start()

    os.makedirs(os.path.abspath(os.path.join(script_dir, log_dir)), exist_ok=True)
    txt_log_filepath = os.path.abspath(os.path.join(script_dir, log_dir, "txt_log.txt"))
    json_log_filepath = os.path.abspath(os.path.join(script_dir, log_dir, "json_log.json"))

    with open(txt_log_filepath, 'a+') as f_txt, open(json_log_filepath, 'a+') as f_json:
        log_ready.set()
        while producer.is_alive():
            # Main loop
            try:
                new_packet = q.get(timeout=0.1)
                new_packet.print_to_file(f_txt)
                #new_packet.print_to_js(f_json)
            except queue.Empty:
                pass

    # Exit
    producer.join()
    f_txt.closed
    f_json.closed