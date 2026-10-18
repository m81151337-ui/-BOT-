
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>VOID HOST</title>
        <style>
            body {
                margin: 0;
                background: #080808;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 70px 20px;
            }
            h1 { color: #00aaff; font-size: 42px; }
            p { color: #bbb; }
            .panel {
                max-width: 420px;
                margin: 30px auto;
                padding: 25px;
                border: 1px solid #087ca7;
                border-radius: 15px;
                background: #111;
            }
        </style>
    </head>
    <body>
        <h1>VOID HOST</h1>
        <p>استضافتك تبدأ من هنا</p>
        <div class="panel">
            <h2>لوحة تحكم البوتات</h2>
            <p>مرحبًا بك في VOID HOST</p>
            <p>قريبًا: إدارة وربط بوتات واتساب</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
