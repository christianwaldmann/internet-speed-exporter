import time
import speedtest
from prometheus_client import start_http_server, Gauge


download_speed = Gauge("download_speed", "Internet download speed in byte/s")
upload_speed = Gauge("upload_speed", "Internet upload speed in byte/s")


st = speedtest.Speedtest()


def get_metrics():
    download_speed_in_bit_per_s = st.download()
    download_speed.set(download_speed_in_bit_per_s)

    upload_speed_in_bit_per_s = st.upload()
    upload_speed.set(upload_speed_in_bit_per_s)


if __name__ == "__main__":
    start_http_server(9000)

    while True:
        get_metrics()
        time.sleep(5 * 60)
