
from flask import Flask, render_template, request
import qrcode
import os
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_image = None
    data = ""

    if request.method == "POST":
        data = request.form.get("data", "").strip()

        if data:
            qr = qrcode.QRCode(
                version=15,  # QR code version
                box_size=10,  # Size of each box
                border=5  # White border
            )

            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(
                fill_color="black",
                back_color="white"
            )

            filename = f"qr_{uuid.uuid4().hex}.png"
            filepath = os.path.join(app.static_folder, filename)
            img.save(filepath)

            qr_image = filename

    return render_template(
        "index.html",
        qr_image=qr_image,
        data=data
    )

if __name__ == "__main__":
    app.run(debug=True)
