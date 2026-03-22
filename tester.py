import requests

def check_headers(url):
    print("\nChecking security headers...")

    try:
        res = requests.get(url)
        headers = res.headers

        important_headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "Strict-Transport-Security"
        ]

        for h in important_headers:
            if h in headers:
                print(f"[+] {h} present")
            else:
                print(f"[!] {h} missing")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    url = input("Enter URL: ")

    if url.startswith("http"):
        check_headers(url)
    else:
        print("Invalid URL")