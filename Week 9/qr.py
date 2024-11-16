import qrcode

text = """RFID (Radio Frequency Identification) is a technology that uses electromagnetic fields to identify and track objects wirelessly. It works through a system that includes an RFID tag (containing a chip and antenna), a reader, and software to process the data. When the tag is near the reader, it transmits information, enabling quick and seamless identification.

Here are some common applications of RFID:
    1.    Inventory Management: Retailers use RFID to keep track of products in real-time, manage stock levels, and reduce theft. For example, clothing items can have embedded RFID tags that help monitor inventory across stores.
    2.    Logistics and Supply Chain: RFID helps track shipments and goods as they move through warehouses and distribution networks, improving efficiency and transparency.
    3.    Access Control: Many offices, parking lots, and secure facilities use RFID cards or key fobs for convenient and secure entry.
    4.    Healthcare: Hospitals use RFID to track medical equipment, monitor patient movements, and ensure accurate medication administration.
    5.    Transportation and Tolling: RFID is widely used in systems like E-ZPass, allowing drivers to pay tolls electronically without stopping.

QR Codes and Their Uses

A QR code (Quick Response code) is a type of two-dimensional barcode that stores information in a grid of black and white squares. It can be scanned with a smartphone or a dedicated QR code reader to quickly access digital content such as links, text, or other data. These codes are simple, affordable, and highly versatile.

Some common uses of QR codes include:
    1.    Marketing and Advertising: Businesses use QR codes to direct customers to product pages, special offers, or promotional content.
    2.    Cashless Payments: Apps like PayPal, Venmo, and WeChat Pay use QR codes for fast and secure transactions.
    3.    Product Identification: Manufacturers include QR codes on items for warranty registration, anti-counterfeiting measures, and product details.
    4.    Transportation: QR codes are often used for boarding passes, train tickets, and event entry tickets.
    5.    Education: Teachers and students use QR codes to access study materials, interactive content, and digital assignments easily.

QR Codes and RFID in Supply Chain Management

Both QR codes and RFID play essential roles in modern supply chain management by improving efficiency, accuracy, and transparency.
    1.    Tracking and Visibility: RFID provides real-time tracking of goods in transit, while QR codes let stakeholders quickly scan and retrieve detailed product information.
    2.    Reducing Errors: RFID automates data collection, reducing the chances of human error during shipping and receiving. QR codes ensure accurate and easily accessible information for all supply chain participants.
    3.    Efficiency: RFID can scan multiple tags at once, speeding up tasks like inventory counts and loading. QR codes allow instant access to documentation and product details with minimal setup.
    4.    Cost-Effectiveness: RFID systems require a higher initial investment but offer long-term savings by streamlining processes and preventing losses. QR codes, on the other hand, are inexpensive to create and maintain, making them ideal for wide use.
    5.    Transparency and Sustainability: Both technologies promote transparency by giving consumers and stakeholders detailed insights into a product’s journey. Additionally, they reduce the need for physical paperwork, supporting more sustainable practices.

Together, RFID and QR codes complement each other in streamlining supply chain operations, reducing waste, and enhancing trust among businesses and consumers."""

# Split the text into smaller chunks
chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

# Generate QR codes for each chunk
for i, chunk in enumerate(chunks):
    img = qrcode.make(chunk)
    img.save(f"qr_code_part_{i+1}.png")