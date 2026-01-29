
import csv
import random
from datetime import datetime
from typing import Dict, List, Tuple
from enum import Enum
from faker import Faker


class ServiceType(Enum):
    CONSULTATION = "CONSULTATION FEES"
    NOTARIZATION = "NOTARIZATION FEES"
    CRIMINAL = "CRIMINAL CASES ACCEPTANCE FEES"
    CIVIL = "CIVIL CASES ACCEPTANCE FEES"
    OTHER_ACCEPTANCE = "OTHER ACCEPTANCE FEES"
    DOMESTIC_CORP = "DOMESTIC CORPORATIONS"
    FOREIGN_CORP = "FOREIGN CORPORATIONS"
    NON_STOCK = "NON-STOCK/NOT-FOR-PROFIT"
    PARTNERSHIP = "PARTNERSHIP"
    SPECIAL = "SPECIAL TRANSACTIONS & DOCUMENTS"
    INSOLVENCY = "INSOLVENCY PROCEEDINGS"
    AGRARIAN = "AGRARIAN RELATION"
    RETAINER = "MONTHLY RETAINER"
    AGENCIES = "FEES BEFORE OTHER AGENCIES"
    APPEARANCE = "APPEARANCE FEES"

fake = Faker()  # defaults to en_US locale

# Data for random names
FIRST_NAMES = [fake.first_name() for _ in range(2500)]
LAST_NAMES = [fake.last_name() for _ in range(2500)]

# Service details for Re: field (EXACTLY as in your data)
SERVICE_DETAILS = {
    ServiceType.CONSULTATION: [
        "Plain Consultation",
        "Consultation with written advice",
        "Research/Preliminary Study",
        "Preparation of Attorney's Letter",
        "Partnership Agreement"
    ],
    ServiceType.NOTARIZATION: [
        "Preparation and notarization of simple affidavits (jurat)",
        "Authentication of documents",
        "Preparation of contracts involving sale",
        "Preparation of contracts not involving sale (no pecuniary consideration)"
    ],
    ServiceType.CRIMINAL: [
        "Criminal Case - Municipal Trial Courts",
        "Criminal Case - Regional Trial Courts",
        "Criminal Case - Court of Appeals",
        "Criminal Case - Supreme Court"
    ],
    ServiceType.CIVIL: [
        "Civil Case - Municipal Trial Courts",
        "Civil Case - Regional Trial Courts",
        "Civil Case - Court of Appeals",
        "Civil Case - Supreme Court"
    ],
    ServiceType.OTHER_ACCEPTANCE: [
        "Correction of entries/Change of Name",
        "Domestic Adoption",
        "Adoption Involving Foreigners (Intercountry Adoption)",
        "Naturalization",
        "Negotiation and Execution of Collective Bargaining Agreement (CBA)",
        "Election Cases",
        "Testate/Intestate Proceedings without Opposition",
        "Testate/Intestate Proceedings with Opposition",
        "Land Registration (with Opposition)",
        "Land Registration (Without Opposition)",
        "Reconstitution of title",
        "New Owner's Duplicate of Title",
        "Registration of patents, copyrights",
        "Immigration"
    ],
    ServiceType.DOMESTIC_CORP: [
        "Simple Articles of Incorporation and By-Laws",
        "Stockholders agreement or voting trust",
        "Amending corporate charter",
        "Preparation of documents for registration to act as registered agent",
        "Preparation of filing corporate reports",
        "Preparation of documents for dissolution of corporations",
        "Preparation of corporate resolution",
        "Change of registered agent or office"
    ],
    ServiceType.FOREIGN_CORP: [
        "Authority to do business in the Philippines",
        "Documents for registration to act as registered agent",
        "Preparation of necessary documents for withdrawal from country",
        "Change of registered agent or office"
    ],
    ServiceType.NON_STOCK: [
        "Articles of Incorporation and By-Laws of non-stock"
    ],
    ServiceType.PARTNERSHIP: [
        "Drafting of Articles of Partnership",
        "Registration of trade name",
        "Dissolution, including notices to creditors and agreements"
    ],
    ServiceType.SPECIAL: [
        "Deed of Donations",
        "Bond, collateral or indemnity",
        "Building Contract",
        "Release or Extension of Mortgage with additional condition",
        "Option to Purchase Real Estate",
        "Preparation and Acknowledgement of Collective Bargaining Agreement"
    ],
    ServiceType.INSOLVENCY: [
        "Insolvency Proceedings - Business",
        "Insolvency Proceedings - Individual",
        "Insolvency Proceedings - Husband and Wife (additional)",
        "Preparations and filing of motion to discharge",
        "Filing creditor's claim",
        "Eminent Domain or Expropriation Proceeding"
    ],
    ServiceType.AGRARIAN: [
        "Agrarian Relation - For landowner",
        "Agrarian Relation - For Tenant"
    ],
    ServiceType.RETAINER: [
        "Monthly Retainer for Legal Services"
    ],
    ServiceType.AGENCIES: [
        "Original Jurisdiction",
        "Appellate Jurisdiction"
    ],
    ServiceType.APPEARANCE: [
        "Municipal Trial Courts Appearance",
        "Regional Trial Courts Appearance",
        "Supreme Court Appearance",
        "Sandiganbayan Appearance",
        "Ombudsman Appearance",
        "Labor Arbiter Appearance",
        "DOLE/POEA/NCMB Appearance",
        "NLRC Appearance",
        "OMB Appearance",
        "Prosecutor's Office Appearance",
        "Other Administrative Agencies Appearance"
    ]
}

# Description text for billing statement
DESCRIPTION_TEXTS = {
    ServiceType.CONSULTATION: [
        "Plain Consultation (per hour)",
        "Consultation with written advice (per hour or per page)",
        "Research/Preliminary Study (per hour)",
        "Preparation of Attorney's Letter",
        "Partnership Agreement (per month)"
    ],
    ServiceType.NOTARIZATION: [
        "Preparation and notarization of simple affidavits (jurat)",
        "Authentication of documents",
        "Preparation of contracts involving sale",
        "Preparation of contracts not involving sale"
    ],
    ServiceType.CRIMINAL: [
        "Criminal Case Acceptance - Municipal Trial Courts",
        "Criminal Case Acceptance - Regional Trial Courts",
        "Criminal Case Acceptance - Court of Appeals",
        "Criminal Case Acceptance - Supreme Court"
    ],
    ServiceType.CIVIL: [
        "Civil Case Acceptance - Municipal Trial Courts",
        "Civil Case Acceptance - Regional Trial Courts",
        "Civil Case Acceptance - Court of Appeals",
        "Civil Case Acceptance - Supreme Court"
    ],
    ServiceType.OTHER_ACCEPTANCE: [
        "Correction of entries/Change of Name",
        "Domestic Adoption Proceedings",
        "Intercountry Adoption Proceedings",
        "Naturalization Proceedings",
        "CBA Negotiation and Execution",
        "Election Case Representation",
        "Testate/Intestate Proceedings without Opposition",
        "Testate/Intestate Proceedings with Opposition",
        "Land Registration (with Opposition)",
        "Land Registration (Without Opposition)",
        "Reconstitution of Title",
        "New Owner's Duplicate of Title",
        "Patent/Copyright Registration",
        "Immigration Services"
    ],
    ServiceType.DOMESTIC_CORP: [
        "Articles of Incorporation and By-Laws Preparation",
        "Stockholders Agreement/Voting Trust",
        "Corporate Charter Amendment",
        "Registered Agent Registration Documents",
        "Corporate Reports Filing Preparation",
        "Corporate Dissolution Documents",
        "Corporate Resolution Preparation",
        "Change of Registered Agent/Office"
    ],
    ServiceType.FOREIGN_CORP: [
        "Authority to Do Business in PH",
        "Foreign Corp Registered Agent Documents",
        "Withdrawal from Country Documents",
        "Change of Registered Agent/Office - Foreign"
    ],
    ServiceType.NON_STOCK: [
        "Non-Stock Articles & By-Laws Preparation"
    ],
    ServiceType.PARTNERSHIP: [
        "Articles of Partnership Drafting",
        "Trade Name Registration",
        "Partnership Dissolution"
    ],
    ServiceType.SPECIAL: [
        "Deed of Donation Preparation",
        "Bond/Collateral/Indemnity Agreement",
        "Building Contract Review/Preparation",
        "Mortgage Release/Extension",
        "Option to Purchase Real Estate",
        "CBA Preparation & Acknowledgement"
    ],
    ServiceType.INSOLVENCY: [
        "Business Insolvency Proceedings",
        "Individual Insolvency Proceedings",
        "Husband & Wife Insolvency (Additional)",
        "Motion to Discharge Preparation",
        "Creditor's Claim Filing",
        "Eminent Domain/Expropriation Proceedings"
    ],
    ServiceType.AGRARIAN: [
        "Agrarian Case - Landowner Representation",
        "Agrarian Case - Tenant Representation"
    ],
    ServiceType.RETAINER: [
        "Monthly Legal Retainer Fee"
    ],
    ServiceType.AGENCIES: [
        "Original Jurisdiction Agency Case",
        "Appellate Jurisdiction Agency Case"
    ],
    ServiceType.APPEARANCE: [
        "Court Appearance - Municipal Trial Courts",
        "Court Appearance - Regional Trial Courts",
        "Court Appearance - Supreme Court",
        "Court Appearance - Sandiganbayan",
        "Court Appearance - Ombudsman",
        "Appearance - Labor Arbiter",
        "Appearance - DOLE/POEA/NCMB",
        "Appearance - NLRC",
        "Appearance - OMB",
        "Appearance - Prosecutor's Office",
        "Appearance - Other Administrative Agencies"
    ]
}

# BASE compensation values (minimum/fixed amounts)
COMPENSATION_BASE = {
    ServiceType.CONSULTATION: [1000, 1000, 1500, 500, 8000],
    ServiceType.NOTARIZATION: [1000, 500, 1500, 1500],
    ServiceType.CRIMINAL: [50000, 75000, 85000, 150000],
    ServiceType.CIVIL: [50000, 75000, 85000, 150000],
    ServiceType.OTHER_ACCEPTANCE: [
        40000, 75000, 150000, 150000, 50000, 120000, 
        60000, 50000, 150000, 75000, 75000, 50000, 
        150000, 50000
    ],
    ServiceType.DOMESTIC_CORP: [
        30000, 30000, 30000, 10000, 6000, 25000,
        3500, 5000
    ],
    ServiceType.FOREIGN_CORP: [35000, 35000, 35000, 25000],
    ServiceType.NON_STOCK: [35000],
    ServiceType.PARTNERSHIP: [35000, 10000, 35000],
    ServiceType.SPECIAL: [20000, 5000, 20000, 3000, 20000, 30000],
    ServiceType.INSOLVENCY: [25000, 50000, 30000, 25000, 10000, 100000],
    ServiceType.AGRARIAN: [80000, 76000],  # RTC rate (75k) + 5k for affidavit / + 1k for tenant
    ServiceType.RETAINER: [8000],
    ServiceType.AGENCIES: [60000, 75000],
    ServiceType.APPEARANCE: [2500, 3500, 20000, 10000, 10000, 2000, 2500, 3000, 2500, 3500, 3500]
}

def generate_random_date() -> str:
    """Generate a random date between 1995 and 2026"""
    year = random.randint(1995, 2026)
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)
    
    try:
        date_obj = datetime(year, month, day)
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return generate_random_date()

def generate_random_name() -> str:
    """Generate a random Filipino name"""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    return f"{first_name} {last_name}"

def format_currency(amount: int) -> str:
    """Format amount as PHP currency"""
    return f"PHP {amount:,.2f}"

def calculate_compensation(service_type: ServiceType, idx: int, base_amount: int) -> int:
    """Calculate the actual compensation based on service type and index"""
    
    if service_type == ServiceType.CONSULTATION:
        if idx == 1:  # Consultation with written advice
            return random.choice([1000, 500 * random.randint(1, 5)])
        elif idx == 4:  # Partnership Agreement (per month)
            return random.randint(8000, 10000)
    
    elif service_type == ServiceType.NOTARIZATION:
        if idx == 1:  # Authentication of documents
            return random.choice([500, 100 * random.randint(1, 10)])
        elif idx == 2:  # Preparation of contracts involving sale
            contract_price = random.randint(50000, 5000000)
            percent_fee = int(contract_price * 0.03)
            return max(percent_fee, 1500)
    
    elif service_type == ServiceType.OTHER_ACCEPTANCE:
        if idx == 4:  # CBA - can be hourly
            if random.choice([True, False]):
                return 50000
            else:
                return 2500 * random.randint(1, 10)
        elif idx == 6:  # Testate/Intestate without opposition
            zonal_value = random.randint(1000000, 10000000)
            percent_fee = int(zonal_value * 0.05)
            return max(percent_fee, 60000)
        elif idx == 7:  # Testate/Intestate with opposition
            fmv = random.randint(1000000, 10000000)
            percent_fee = int(fmv * 0.10)
            return max(percent_fee, 50000)
        elif idx == 8:  # Land Registration with Opposition
            fmv = random.randint(1000000, 20000000)
            percent_fee = int(fmv * 0.05)
            return max(percent_fee, 150000)
        elif idx == 9:  # Land Registration without Opposition
            fmv = random.randint(1000000, 20000000)
            percent_fee = int(fmv * 0.05)
            return max(percent_fee, 75000)
    
    elif service_type == ServiceType.DOMESTIC_CORP:
        if idx == 0:  # Articles of Incorporation
            capital = random.randint(1000000, 50000000)
            extra_millions = max(0, (capital - 1000000) // 1000000)
            return 30000 + (extra_millions * 4000)
    
    elif service_type == ServiceType.PARTNERSHIP:
        if idx == 0:  # Drafting Articles of Partnership
            capital = random.randint(1000000, 20000000)
            extra_millions = max(0, (capital - 1000000) // 1000000)
            return 35000 + (extra_millions * 5000)
    
    elif service_type == ServiceType.SPECIAL:
        if idx == 0:  # Deed of Donations
            zonal_value = random.randint(500000, 5000000)
            percent_fee = int(zonal_value * 0.03)
            return max(percent_fee, 20000)
        elif idx == 2:  # Building Contract
            contract_value = random.randint(500000, 10000000)
            percent_fee = int(contract_value * 0.03)
            return max(percent_fee, 20000)
        elif idx == 4:  # Option to Purchase Real Estate
            purchase_price = random.randint(1000000, 10000000)
            percent_fee = int(purchase_price * 0.03)
            return max(percent_fee, 20000)
    
    elif service_type == ServiceType.INSOLVENCY:
        if idx == 5:  # Eminent Domain
            agreed_amount = random.randint(500000, 5000000)
            percent_fee = int(agreed_amount * 0.10)
            return max(percent_fee, 100000)
    
    elif service_type == ServiceType.AGRARIAN:
        affidavits = random.randint(1, 5)
        if idx == 0:  # Landowner
            return 75000 + (5000 * affidavits)
        else:  # Tenant
            return 75000 + (1000 * affidavits)
    
    elif service_type == ServiceType.APPEARANCE:
        # For appearance fees, sometimes use hourly rate
        hourly_rates = [1000, 1500, 5000, 5000, 3000, 1000, 1500, 1500, 1500, 1500, 1500]
        if random.choice([True, False]):
            hours = random.randint(1, 8)
            return hourly_rates[idx] * hours
        else:
            return base_amount
    
    return base_amount

def generate_invoice() -> Tuple[str, int]:
    """Generate a complete invoice with 1-7 services and return the text and total compensation"""
    
    # Generate random data for the invoice header
    attention_name = generate_random_name()
    date = generate_random_date()
    
    # Random number of services in this invoice (1-7)
    num_services = random.randint(1, 7)
    
    # Generate random law firm name
    law_firm_name = f"{random.choice(LAST_NAMES)} {random.choice(LAST_NAMES)} & {random.choice(LAST_NAMES)} Law Office"
    
    # Collect services for this invoice
    services = []
    total_compensation = 0
    
    for _ in range(num_services):
        # Randomly select a service type
        service_type = random.choice(list(ServiceType))
        
        # Get index for service details, description, and compensation
        idx = random.randint(0, len(SERVICE_DETAILS[service_type]) - 1)
        
        # Get the data
        service_detail = SERVICE_DETAILS[service_type][idx]
        description = DESCRIPTION_TEXTS[service_type][idx]
        base_compensation = COMPENSATION_BASE[service_type][idx]
        
        # Calculate actual compensation
        compensation = calculate_compensation(service_type, idx, base_compensation)
        qty = random.randint(1, 10)
        service_total = compensation * qty
        
        # Add to services list
        services.append({
            'description': description,
            'qty': qty,
            'unit_price': compensation,
            'service_total': service_total,
            'service_detail': service_detail
        })
        
        total_compensation += service_total
    
    # Choose the main service detail for the "Re:" field (first one or a summary)
    if num_services == 1:
        main_service_detail = services[0]['service_detail']
    elif num_services <= 3:
        main_service_detail = f"Multiple Legal Services ({num_services} items)"
    else:
        main_service_detail = f"Comprehensive Legal Services Package ({num_services} items)"
    
    # Create the invoice text (all on one line with spaces)
    # Start with the header
    invoice_text = (
        f"Attention: {attention_name} "
        f"Date: {date} "
        f"Re: {main_service_detail} "
        f"Please see the attached invoice for legal services below rendered by {law_firm_name} "
        "Office. For any questions or clarifications, feel free to contact us. "
        "Thank you for your trust. "
        "BILLING STATEMENT "
        "Description Qty Unit Price Amount "
    )
    
    # Add each service line
    for service in services:
        invoice_text += (
            f"{service['description']} {service['qty']} "
            f"{format_currency(service['unit_price'])} "
            f"{format_currency(service['service_total'])} "
        )
    
    # Add the subtotal
    invoice_text += f"Subtotal: {format_currency(total_compensation)}"
    
    return invoice_text, total_compensation

def create_csv_file(num_rows: int = 10, filename: str = "legal_invoices.csv"):
    """Create a CSV file with generated invoice data"""
    
    data = []
    for _ in range(num_rows):
        invoice_text, _ = generate_invoice()
        data.append({
            "text": invoice_text,
            "category": "LEGAL_FEES",
            "label": "2",
        })
    
    # Write to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['text', 'category', 'label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow({'text': row['text'], 'category': row['category'], 'label': row['label']})
    
    print(f"Created {filename} with {num_rows} rows of data.")
    
def display_service_categories():
    """Display all service categories and counts"""
    print("\nService Categories Available:")
    print("=" * 50)
    for service_type in ServiceType:
        count = len(SERVICE_DETAILS[service_type])
        print(f"{service_type.value}: {count} services")
    print("=" * 50)

def main():
    """Main function to run the program"""
    display_service_categories()
    
    try:
        num_rows = 800
        
        filename = input("Enter output filename (default 'legal_invoices.csv'): ") or "legal_invoices.csv"
        
        print("\nGenerating invoices...")
        create_csv_file(num_rows, filename)
        
        print(f"\n✓ Successfully generated {num_rows} invoice records!")
        print(f"✓ File saved as: {filename}")
        print(f"✓ All records labeled as: 'legal_fees'")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()