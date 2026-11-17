import os

# Las credenciales de Transbank se leen desde variables de entorno (.env),
# nunca se escriben directamente en el código.
TBK_API_KEY = os.environ.get('TRANSBANK_API_KEY', '')
TBK_MALL_ID = os.environ.get('TRANSBANK_MALL_ID', '')
TBK_COMMERCE_CODE = os.environ.get('TRANSBANK_COMMERCE_CODE', '')
TBK_INTEGRATION_TYPE = os.environ.get('TRANSBANK_INTEGRATION_TYPE', 'TEST')
