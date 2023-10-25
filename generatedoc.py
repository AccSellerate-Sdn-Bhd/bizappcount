from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
import io
def generate_professional_pdf_from_sale(sale,line_items):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()

    # 1. Header
    # Assuming company_info is a dictionary with keys: 'logo', 'name', 'address', 'phone', 'email'
    #if company_info.get('logo'):
        #logo = Image(company_info['logo'])
        #logo.drawHeight = 1.25*inch
        #logo.drawWidth = 2.5*inch
        #elements.append(logo)
    
    company_name = Paragraph("Test Company", styles['Heading1'])
    company_contact = Paragraph(f"Address: Test Address<br/>Phone: 011111111111<br/>Email: test@gmail.com", styles['BodyText'])
    elements.extend([company_name, company_contact])

    # 2. Client Information
    # Assuming client_info is a dictionary with keys: 'name', 'address', 'phone', 'email'
    client_data = [
        ["Client Name", "Client Name"],
        ["Address", "Test Address"],
        ["Phone", "011111111111"],
        ["Email", "test@gmail.com"]
    ]
    client_table = Table(client_data, colWidths=[2*inch, 4.5*inch])
    elements.append(client_table)

    # 3. Quotation Details
    elements.append(Paragraph("Quotation Details", styles['Heading2']))
    quote_data = [
        ["Quotation ID", sale.sales_id],
        ["Date", sale.date.strftime("%Y-%m-%d")],
        ["Salesperson", "TODO"],  # Replace TODO with actual salesperson name if available
        ["Document Number", sale.document_number if sale.document_number else "N/A"]
    ]
    quote_table = Table(quote_data, colWidths=[2.5*inch, 4*inch])
    elements.append(quote_table)

    # 4. List of Products/Services
    elements.append(Paragraph("Product/Service Line Items", styles['Heading2']))

    line_data = [["Description", "Quantity", "Unit Price", "Total"]]
    for item in line_items:
        description = getattr(item.product_id, "name", "Product Name")  # using getattr to provide a default
        unit_price = item.product_id.cost  # Assuming there's a price attribute in Product
        total_price_for_item = item.total_price
        
        line_data.append([description, item.quantity, f"${unit_price:.2f}", f"${total_price_for_item:.2f}"])

    line_table = Table(line_data, colWidths=[3*inch, 1.5*inch, 2*inch, 1.5*inch])
    elements.append(line_table)

    # 5. Footer
    # Calculate the total amounts and taxes
    total_amount = sum(item.total_price for item in line_items)
    taxes = 0.10 * total_amount  # Example: 10% tax
    grand_total = total_amount + taxes

    total_data = [
        ["Total Amount", f"${total_amount:.2f}"],
        ["Taxes (10%)", f"${taxes:.2f}"],
        ["Grand Total", f"${grand_total:.2f}"]
    ]
    total_table = Table(total_data, colWidths=[2.5*inch, 4*inch])
    elements.append(total_table)

    # Thank You Note & Additional Notes
    thank_you_note = Paragraph("Thank you for doing business with us!", styles['Italic'])
    terms_conditions = Paragraph("Terms & Conditions: Delivery within 30 days of purchase. Returns allowed within 15 days.", styles['BodyText'])
    elements.extend([thank_you_note, terms_conditions])

    doc.build(elements)
    buffer.seek(0)

    return buffer


def generate_professional_invoice_from_sale(sale, line_items):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()

    # 1. Header
    company_name = Paragraph("Test Company", styles['Heading1'])
    company_contact = Paragraph(f"Address: Test Address<br/>Phone: 011111111111<br/>Email: test@gmail.com", styles['BodyText'])
    elements.extend([company_name, company_contact])

    # 2. Client Information
    client_data = [
        ["Client Name", "Client Name"],
        ["Address", "Test Address"],
        ["Phone", "011111111111"],
        ["Email", "test@gmail.com"]
    ]
    client_table = Table(client_data, colWidths=[2*inch, 4.5*inch])
    elements.append(client_table)

    # 3. Invoice Details
    elements.append(Paragraph("Invoice Details", styles['Heading2']))
    invoice_data = [
        ["Invoice ID", sale.sales_id],
        ["Date", sale.date.strftime("%Y-%m-%d")],
        ["Salesperson", "TODO"],
        ["Document Number", sale.document_number if sale.document_number else "N/A"]
    ]
    invoice_table = Table(invoice_data, colWidths=[2.5*inch, 4*inch])
    elements.append(invoice_table)

    # 4. List of Products/Services Sold
    elements.append(Paragraph("Product/Service Line Items", styles['Heading2']))

    line_data = [["Description", "Quantity", "Unit Price", "Total"]]
    for item in line_items:
        description = getattr(item.product_id, "name", "Product Name")
        unit_price = item.product_id.cost
        total_price_for_item = item.total_price
        
        line_data.append([description, item.quantity, f"${unit_price:.2f}", f"${total_price_for_item:.2f}"])

    line_table = Table(line_data, colWidths=[3*inch, 1.5*inch, 2*inch, 1.5*inch])
    elements.append(line_table)

    # 5. Totals & Payment Details
    total_amount = sum(item.total_price for item in line_items)
    taxes = 0.10 * total_amount  # Example: 10% tax
    grand_total = total_amount + taxes

    total_data = [
        ["Total Amount", f"${total_amount:.2f}"],
        ["Taxes (10%)", f"${taxes:.2f}"],
        ["Grand Total", f"${grand_total:.2f}"]
    ]
    total_table = Table(total_data, colWidths=[2.5*inch, 4*inch])
    elements.append(total_table)

    # Payment Terms & Notes
    payment_terms = Paragraph("Payment Terms: Due within 30 days of receipt of invoice.", styles['BodyText'])
    notes_conditions = Paragraph("Notes: Please make the payment to our bank account. Returns are not permitted.", styles['BodyText'])
    elements.extend([payment_terms, notes_conditions])

    doc.build(elements)
    buffer.seek(0)

    return buffer


def generate_professional_delivery_order(sale, line_items):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()

    # 1. Header
    company_name = Paragraph("Test Company", styles['Heading1'])
    company_contact = Paragraph(f"Address: Test Address<br/>Phone: 011111111111<br/>Email: test@gmail.com", styles['BodyText'])
    elements.extend([company_name, company_contact])

    # 2. Client Information
    client_data = [
        ["Client Name", "Client Name"],
        ["Delivery Address", "Test Address"],
        ["Phone", "011111111111"],
        ["Email", "test@gmail.com"]
    ]
    client_table = Table(client_data, colWidths=[2*inch, 4.5*inch])
    elements.append(client_table)

    # 3. DO Details
    elements.append(Paragraph("Delivery Order Details", styles['Heading2']))
    do_data = [
        ["DO ID", sale.sales_id],
        ["Date", sale.date.strftime("%Y-%m-%d")],
        ["Salesperson", "TODO"],
        ["Document Number", sale.document_number if sale.document_number else "N/A"]
    ]
    do_table = Table(do_data, colWidths=[2.5*inch, 4*inch])
    elements.append(do_table)

    # 4. List of Products/Services to Deliver
    elements.append(Paragraph("Product/Service Line Items for Delivery", styles['Heading2']))

    line_data = [["Description", "Quantity"]]
    for item in line_items:
        description = getattr(item.product_id, "name", "Product Name")
        
        line_data.append([description, item.quantity])

    line_table = Table(line_data, colWidths=[5*inch, 2*inch])
    elements.append(line_table)

    # Delivery Notes or Instructions
    delivery_notes = Paragraph("Please handle with care and ensure all items are checked upon receipt.", styles['Italic'])
    elements.extend([delivery_notes])

    doc.build(elements)
    buffer.seek(0)

    return buffer


def generate_professional_receipt(sale, line_items):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()

    # 1. Header
    company_name = Paragraph("Test Company", styles['Heading1'])
    company_contact = Paragraph(f"Address: Test Address<br/>Phone: 011111111111<br/>Email: test@gmail.com", styles['BodyText'])
    elements.extend([company_name, company_contact])

    # 2. Client Information
    client_data = [
        ["Client Name", "Client Name"],
        ["Address", "Test Address"],
        ["Phone", "011111111111"],
        ["Email", "test@gmail.com"]
    ]
    client_table = Table(client_data, colWidths=[2*inch, 4.5*inch])
    elements.append(client_table)

    # 3. Receipt Details
    elements.append(Paragraph("Receipt Details", styles['Heading2']))
    receipt_data = [
        ["Receipt ID", sale.sales_id],
        ["Date", sale.date.strftime("%Y-%m-%d")],
        ["Salesperson", "TODO"],
        ["Document Number", sale.document_number if sale.document_number else "N/A"]
    ]
    receipt_table = Table(receipt_data, colWidths=[2.5*inch, 4*inch])
    elements.append(receipt_table)

    # 4. List of Purchased Products/Services
    elements.append(Paragraph("Purchased Product/Service Line Items", styles['Heading2']))

    line_data = [["Description", "Quantity", "Unit Price", "Total"]]
    for item in line_items:
        description = getattr(item.product_id, "name", "Product Name")
        unit_price = item.product_id.cost  # Assuming there's a price attribute in Product
        total_price_for_item = item.total_price
        
        line_data.append([description, item.quantity, f"${unit_price:.2f}", f"${total_price_for_item:.2f}"])

    line_table = Table(line_data, colWidths=[3*inch, 1.5*inch, 2*inch, 1.5*inch])
    elements.append(line_table)

    # 5. Total Amount Paid
    total_amount = sum(item.total_price for item in line_items)
    total_data = [
        ["Total Amount Paid", f"${total_amount:.2f}"]
    ]
    total_table = Table(total_data, colWidths=[2.5*inch, 4*inch])
    elements.append(total_table)

    # Thank You Note
    thank_you_note = Paragraph("Thank you for your purchase!", styles['Italic'])
    elements.extend([thank_you_note])

    doc.build(elements)
    buffer.seek(0)

    return buffer


def generate_professional_purchase_order(expense, line_items):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()

    # 1. Header
    company_name = Paragraph("Test Company", styles['Heading1'])
    company_contact = Paragraph(f"Address: Test Address<br/>Phone: 011111111111<br/>Email: test@gmail.com", styles['BodyText'])
    elements.extend([company_name, company_contact])

    # 2. Supplier Information
    supplier_data = [
        ["Supplier Name", "Supplier Name"],
        ["Address", "Supplier Address"],
        ["Phone", "Supplier Phone Number"],
        ["Email", "Supplier Email"]
    ]
    supplier_table = Table(supplier_data, colWidths=[2*inch, 4.5*inch])
    elements.append(supplier_table)

    # 3. PO Details
    elements.append(Paragraph("Purchase Order Details", styles['Heading2']))
    po_data = [
        ["PO ID", expense.expense_id],
        ["Date", expense.date.strftime("%Y-%m-%d")],
        ["Buyer", "Your Company Name"],
        ["Document Number", expense.expense_id if expense.expense_id else "N/A"]
    ]
    po_table = Table(po_data, colWidths=[2.5*inch, 4*inch])
    elements.append(po_table)

    # 4. List of Ordered Products/Services
    elements.append(Paragraph("Ordered Product/Service Line Items", styles['Heading2']))

    line_data = [["Description", "Quantity", "Unit Price", "Total"]]
    for item in line_items:
        description = getattr(item.product_id, "name", "Product Name")
        unit_price = item.product_id.cost
        total_price_for_item = item.total_price
        
        line_data.append([description, item.quantity, f"${unit_price:.2f}", f"${total_price_for_item:.2f}"])

    line_table = Table(line_data, colWidths=[3*inch, 1.5*inch, 2*inch, 1.5*inch])
    elements.append(line_table)

    # 5. Total Amount
    total_amount = sum(item.total_price for item in line_items)
    total_data = [
        ["Total Amount", f"${total_amount:.2f}"]
    ]
    total_table = Table(total_data, colWidths=[2.5*inch, 4*inch])
    elements.append(total_table)

    # Terms & Conditions
    terms_conditions = Paragraph("Terms & Conditions: Goods to be delivered within 30 days of order. Payment to be made within 15 days of delivery.", styles['BodyText'])
    elements.extend([terms_conditions])

    doc.build(elements)
    buffer.seek(0)

    return buffer
