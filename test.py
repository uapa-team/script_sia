from SIARetrieve import sia


soup = sia.get_ha_per("1000221830")
#print(soup.proc)
print(soup.parser.get_historias())
print(soup.parser.get_programa())
print(soup.parser.get_expediente())
