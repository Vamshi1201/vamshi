import psutil
import time

UPDATE_DELAY = 1  # in seconds

def get_size(bytes):
    """Returns size of bytes in a nice format."""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

while True:
    # Get the network I/O stats from psutil
    io = psutil.net_io_counters()
    # Extract the total bytes sent and received
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

    # Sleep for `UPDATE_DELAY` seconds
    time.sleep(UPDATE_DELAY)

    # Get the stats again
    io_2 = psutil.net_io_counters()
    # Calculate the speed
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

    # Print the total download/upload along with current speeds
    print(f"Upload: {get_size(io_2.bytes_sent)}    "
          f"Download: {get_size(io_2.bytes_recv)}    "
          f"Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
          f"Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")

    # Update the bytes_sent and bytes_recv for the next iteration
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
