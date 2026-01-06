from pillow import Image
def melhora imagem  (input_path, output_path):
    # Abre a imagem
    img = Image.open("area de trabalho/site_faul/img/fundo")
    
    # Aplica melhorias na imagem
    img = img.convert("L")  # Converte para escala de cinza
    img = img.filter(Image.Filter.SHARPEN)  # Aplica filtro de nitidez
    
    # Salva a imagem melhorada
    img.save(output_path)