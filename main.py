import warnings
from digital_certificate.cert import Certificate
from dotenv import load_dotenv
import os

warnings.simplefilter("ignore")

load_dotenv()

certificate_name = os.getenv("CERTIFICATE_NAME")
password = os.getenv("CERTIFICATE_PASSWORD")
pfx_file = f"./certificates/{certificate_name}.pfx"

_cert = Certificate(pfx_file=str(pfx_file), password=bytes(f"{password}", "utf-8"))

try:
    _cert.read_pfx_file()

    serial_number = _cert.serial_number()
    created_date = _cert.not_valid_before().strftime("%d/%m/%Y")
    valid_date = _cert.not_valid_after().strftime("%d/%m/%Y")
    owner = _cert.common_name()
    creator = _cert.issuer()

    print(f"Serial Number: {serial_number}")
    print(f"Create Date: {created_date}")
    print(f"Valid Date: {valid_date}")
    print(f"Owner: {owner}")
    print(f"Creator: {creator}")

except Exception as e:
    print(f"Error: {e}")
