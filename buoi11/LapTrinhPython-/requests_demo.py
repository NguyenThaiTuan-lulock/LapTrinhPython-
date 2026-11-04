import requests

# 1. Gọi API công khai của GitHub (thông tin repository Python)
response = requests.get("https://api.github.com/repos/python/cpython")

if response.status_code == 200:
    du_lieu = response.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response.status_code)

print("-" * 40)

# 2. Gọi API tỷ giá ngoại tệ (USD sang VND)
response_rate = requests.get("https://open.er-api.com/v6/latest/USD")

if response_rate.status_code == 200:
    du_lieu_rate = response_rate.json()
    ty_gia_vnd = du_lieu_rate["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi:", response_rate.status_code)