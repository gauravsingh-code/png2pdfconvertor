# from flask import Flask, render_template, request, send_file
from flask import Flask, render_template, send_from_directory, request, send_file
from PIL import Image
import os

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def upload_file():
    return render_template("upload.html")

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


import os

@app.route("/convert", methods=["POST"])
def convert_file():
    files = request.files.getlist("file")
    if not files:
        return "No file uploaded!", 400  # Return an error if no file is uploaded

    images = [Image.open(file).convert("RGB") for file in files]
    
    output_pdf = os.path.join(os.getcwd(), "converted.pdf")  # Ensure absolute path
    images[0].save(output_pdf, save_all=True, append_images=images[1:])  # Save PDF

    print(f"✅ File created: {output_pdf}")  # Debugging: Check if file is created
    
    if not os.path.exists(output_pdf):  # Check if file exists before sending
        return "Error: PDF file not created!", 500

    return send_file(output_pdf, as_attachment=True)




# @app.route("/convert", methods=["POST"])
# def convert_file():
#     files = request.files.getlist("file")  # Get uploaded files
#     images = [Image.open(file).convert("RGB") for file in files]  # Convert to RGB

#     output_pdf = "converted.pdf"
#     images[0].save(output_pdf, save_all=True, append_images=images[1:])  # Save as PDF
    
#     return send_file(output_pdf, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
