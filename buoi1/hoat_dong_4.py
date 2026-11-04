# ========================================
# HOAT DONG 4 - TU KHOA (KEYWORD)
# ========================================

import keyword

print("========== HOAT DONG 4 ==========")

print("Danh sach tu khoa Python:")
print(keyword.kwlist)

print("So luong tu khoa:", len(keyword.kwlist))

print("\nKiem tra mot so tu:")
print("class la keyword:", keyword.iskeyword("class"))
print("True la keyword:", keyword.iskeyword("True"))
print("False la keyword:", keyword.iskeyword("False"))
print("None la keyword:", keyword.iskeyword("None"))
print("diem_toan la keyword:", keyword.iskeyword("diem_toan"))
