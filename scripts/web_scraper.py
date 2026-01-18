import requests

url = "https://www.cnbc.com/world/?region=world"

def main():
	response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
	response.raise_for_status()

	output_path = "data/raw_data/web_data.html"
	with open(output_path, "w", encoding="utf-8") as f:
		f.write(response.text)

	print(f"Saved Html to {output_path}")


if __name__ == "__main__":
	main()
