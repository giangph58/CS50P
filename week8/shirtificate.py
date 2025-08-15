from fpdf import FPDF, XPos, YPos


class ShirtificatePDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")

    def header(self):
        self.set_font("Times", "B", 36)
        self.cell(0, 20, "CS50 Shirtificate", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)


def main():
    name = input("Name: ")

    pdf = ShirtificatePDF()
    pdf.add_page()

    # Add the shirt image centered horizontally
    # A4 width is 210mm, so center the image
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # Add the user's name on top of the shirt in white text
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.set_xy(0, 140)  # Position over the shirt
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    # Save the PDF
    pdf.output("shirtificate.pdf")
    print("shirtificate.pdf created successfully!")


if __name__ == "__main__":
    main()
