import qrcode

# Read the URL from qr.txt
with open('qr.txt', 'r') as file:
    url = file.read().strip()

# Generate the QR code
qr = qrcode.QRCode(
    version=6,  # Use version 40 for large data
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color='black', back_color='white')

# Save the image
img.save('qr_code.png')

print("QR code generated and saved as qr_code.png")