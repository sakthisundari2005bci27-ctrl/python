import speedtest

st = speedtest.Speedtest()
print("Testing Download Speed...")
download = st.download() / 1_000_000 # Convert to Mbps
print(f"Download: {download:.2f} Mbps")

print("Testing Upload Speed...")
upload = st.upload() / 1_000_000
print(f"Upload: {upload:.2f} Mbps")

