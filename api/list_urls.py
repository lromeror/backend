from firebase_admin import db

# Verifica si puedes acceder al documento
ref = db.reference('datos-collections/-OG8H3NMhwA3f505C-Uk')
data = ref.get()

if data is None:
    print("Documento no encontrado")
else:
    print(data)
