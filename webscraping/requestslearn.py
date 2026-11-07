import requests

def downloadpage(url, filename):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
            print(f"✅ Saved to {filename}")
            print(f"   Size: {len(response.text)} characters")

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print(" ❌ Cannot connect!")

downloadpage("https://en.wikipedia.org/wiki/Statue_of_Unity", "statueofunity.txt")


with open("statueofunity.txt",'r',encoding="utf-8") as  f:
    print(f.read()),