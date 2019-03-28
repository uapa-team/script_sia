from SIARetrieve import sia


ha = sia.get_ha_prog("2545", "0", "1000221830")

print(ha.resumen)

#print(ha.proc)
#print(ha.parser.get_historias())
#print(ha.parser.get_programa())
#print(ha.parser.get_expediente())
