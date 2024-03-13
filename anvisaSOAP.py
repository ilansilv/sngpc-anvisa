import requests
import xml.etree.ElementTree as ET

email = "ilansilva001@gmail.com"
senha = "teste123"

url = "https://sngpc.anvisa.gov.br/webservice/sngpc.asmx"

SOAPEnvelope = f"""<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ValidarUsuario xmlns="http://tempuri.org/">
      <E-mail> {email} </E-mail>
      <Senha> {senha} </Senha>
    </ValidarUsuario>
  </soap:Body>
</soap:Envelope>"""

options = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "http://tempuri.org/ValidarUsuario"
}


response = requests.post(url, data = SOAPEnvelope, headers = options)
root = ET.fromstring(response.text)

for child in root.iter("*"):
    validarUsuario = child.text

print(validarUsuario)