import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(long_url)
        print(f"Shortened URL: {short_url}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    url = input("Enter the long URL: ")
    shorten_url(url)
