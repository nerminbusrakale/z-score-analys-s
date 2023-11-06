from scipy.stats import norm

mu = 120  # Ortalama değer
sigma = 25  # Standart sapma

x_alt = 80  # Alt sınır
x_üst = 130  # Üst sınır

# Z-skorları hesapla
z_alt = (x_alt - mu) / sigma
z_üst = (x_üst - mu) / sigma

# İstenen aralıktaki olasılığı hesapla
olasılık = norm.cdf(z_üst) - norm.cdf(z_alt)

# Z-skorlarını yazdır
print("Z-skor (Alt):", z_alt)
print("Z-skor (Üst):", z_üst)

# Olasılığı yazdır
print("Olasılık:", olasılık)
