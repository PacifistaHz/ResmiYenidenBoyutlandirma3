from PIL import Image
import io

# Open the image file
dosyaAdi = "1.jpg"
resim = Image.open(dosyaAdi)

# Convert the image to PNG and calculate its size
out = io.BytesIO()
resim.save(out, format='PNG')
print(f"İlk resim kapladığı alan: {out.tell()/1024:.2f} KB")

# Print the original dimensions of the image
print("İlk resim ebatlari: " + str(resim.size))

# Resize the image
yeniYukseklik = 480
yeniBoyutOrani = (yeniYukseklik / float(resim.size[1]))
yeniGenislik = int((float(resim.size[0]) * float(yeniBoyutOrani)))
resim = resim.resize((yeniGenislik, yeniYukseklik), Image.Resampling.LANCZOS)
print("Son resim ebatlari: " + str(resim.size))

# Save the resized image in JPEG format and calculate its size
resim.save("resim1.jpg")
out = io.BytesIO()
resim.save(out, format='JPEG')
print(f"Son resim kapladığı alan: {out.tell()/1024:.2f} KB")
