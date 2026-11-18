import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sach.csv")
print(df)


tong_dau_sach = len(df)
gia_trung_binh = df["Gia"].mean()
gia_cao_nhat = df["Gia"].max()
sach_gia_cao_nhat = df[df["Gia"] == gia_cao_nhat]["TenSach"].values[0]

print("Tong so dau sach:", tong_dau_sach)
print("Gia trung binh:", gia_trung_binh)
print("Ten sach co gia cao nhat:", sach_gia_cao_nhat)


plt.bar(df["MaSach"], df["SoLuong"])
plt.title("So luong ton kho cua tung cuon sach")
plt.xlabel("Ma sach")
plt.ylabel("So luong")
plt.savefig("bieudo.png")


sach_sap_het = df[df["SoLuong"] < 10]
sach_sap_het.to_csv("canh_bao_sach.csv", index=False)