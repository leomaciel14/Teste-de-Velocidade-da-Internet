import speedtest

def test_velocidade_internet():
    st = speedtest.Speedtest()

    print("Teste Iniciado, aguarde...")

    download_speed = st.download() / 1_000_000
    print(f"Velocidade de Download: {download_speed:.2f} Mbps")

    upload_speed = st.upload() / 1_000_000
    print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")

    server = st.get_best_server()
    ping = server["latency"]
    print(f"Ping: {ping} ms")

    print("Teste Finalizado!")

test_velocidade_internet()