from pystrich.datamatrix import DataMatrixEncoder
from pystrich.code128 import Code128Encoder

# CEP destino -------------------------- 8
# Complemento do CEP ------------------- 5
# CEP origem --------------------------- 8
# Complemento do CEP ------------------- 5
# Validador do CEP destino ------------- 1
# IDV ---------------------------------- 2
# Código de Rastreamento --------------- 13
# Serviços Adicionais (AR, MP, DD, VD) - 8
# Cartão de Postagem ------------------- 10
# Código do Serviço -------------------- 5
# Informação de Agrupamento ------------ 2
# Número do Logradouro ----------------- 5
# Complemento do Logradouro ------------ 20
# Valor Declarado ---------------------- 5
# DDD + Telefone Destinatário ---------- 12
# Latitude ----------------------------- 10
# Longitude ---------------------------- 10
# Pipe "|" ----------------------------- 1
# Reserva para cliente ----------------- 30
encoder_dm = DataMatrixEncoder('12221150000001620312500000651OO382192458BR0000000000000075022907041621I0000000000000000000000000000000000000|')
encoder_dm.save( 'matrix.png' )

# codigo de rastreio
cod_rastreio = Code128Encoder('OO382192458BR')
cod_rastreio.save( 'cod_rastreio.png' )

# cep de destino
cep_destino = Code128Encoder('12221150')
cep_destino.save( 'cep_destino.png' )