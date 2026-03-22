import requests

print("=== Web Security Testing Tool ===")


def check_headers(url):
    print("\nChecking security headers...\n")

    try:
        res = requests.get(url, timeout=10)
        headers = res.headers

        security_headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "Strict-Transport-Security"
        ]

        found = False

        for header in security_headers:
            if header in headers:
                print(f"[+] {header} is present")
                found = True
            else:
                print(f"[!] {header} is missing")

        if found:
            print("\n[+] Some security headers are properly configured")
        else:
            print("\n[!] No major security headers found")

    except requests.exceptions.Timeout:
        print("[!] Request timed out")

    except requests.exceptions.ConnectionError:
        print("[!] Connection error")


if __name__ == "__main__":
    url = input("\nEnter URL: ")

    if url.startswith("http"):
        check_headers(url)
    else:
        print("Invalid URL")