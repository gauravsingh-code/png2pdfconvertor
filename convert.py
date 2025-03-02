from PIL import Image
import os

def png_to_pdf(png_path, pdf_path):
    """Converts a single PNG image to a PDF."""
    try:
        image = Image.open(png_path).convert("RGB")  # Convert PNG to RGB
        image.save(pdf_path)
        print(f"✅ Converted: {png_path} → {pdf_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

def multiple_pngs_to_pdf(png_files, output_pdf):
    """Merges multiple PNG images into a single PDF."""
    try:
        if not png_files:
            print("❌ No PNG files provided!")
            return
        
        images = [Image.open(png).convert("RGB") for png in png_files]
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"✅ Merged {len(png_files)} PNGs into {output_pdf}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Example Usage
    single_png = "sample.png"  # Replace with your PNG file
    output_pdf = "output.pdf"

    if os.path.exists(single_png):
        png_to_pdf(single_png, output_pdf)
    else:
        print(f"❌ File not found: {single_png}")

    # Convert Multiple PNGs to PDF
    png_files = ["img1.png", "img2.png", "img3.png"]  # Replace with your PNG files
    merged_pdf = "merged.pdf"

    # Check if all files exist before merging
    if all(os.path.exists(f) for f in png_files):
        multiple_pngs_to_pdf(png_files, merged_pdf)
    else:
        print("❌ Some files not found. Check file names.")


















# from PIL import Image

# def png_to_pdf(png_path, pdf_path):
#     image = Image.open(png_path)
#     image = image.convert("RGB")  # Convert PNG to RGB mode (necessary for PDF)
#     image.save(pdf_path)
#     print(f"✅ Converted {png_path} to {pdf_path}")

# # Example usage
# png_file = "sample.png"  # Change this to your PNG file
# pdf_file = "output.pdf"
# png_to_pdf(png_file, pdf_file)
