from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
import io
def generate_pdf_from_sale(sale):
    # Create a byte buffer to store the PDF data
    buffer = io.BytesIO()

    # Create a new Document
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    # Create an empty list to store the PDF elements
    elements = []

    # Use built-in styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["BodyText"]

    # Add a title to the PDF
    title = Paragraph("Quotation", title_style)
    elements.append(title)

    # Sales Data as a Table
    sales_data = [
        ["Transaction ID", "Title", "BizApp Transaction No", "Date"], # Headers
        [sale.sales_id, sale.title, sale.bizapp_transaction_no, sale.date.strftime("%Y-%m-%d")] # Data from the sale
    ]

    # Create a table using the sales data
    sales_table = Table(sales_data, colWidths=[2*inch]*4)
    sales_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#E5E5E5'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), '#FFFFFF'),
        ('GRID', (0, 0), (-1, -1), 1, "#D5D5D5"),
    ]))
    elements.append(sales_table)

    # TODO: You can add more information, such as line items, customer data, etc. similar to the above

    # Build the PDF with the elements
    doc.build(elements)

    # Move the buffer position to the beginning
    buffer.seek(0)

    return buffer
