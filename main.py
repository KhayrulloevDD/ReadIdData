import easyocr


# detect russian characters
reader = easyocr.Reader(['ru'], gpu=False) # need to run only once to load model into memory
result_f = reader.readtext('images/id_d_f.jpg', detail=0, text_threshold=0.9)
result_b = reader.readtext('images/id_d_b.jpg', detail=0, text_threshold=0.9)
print(f'front side(russian) \n {result_f} \n back side (russian) \n {result_b}')

# detect english characters
reader = easyocr.Reader(['en'], gpu=False) # need to run only once to load model into memory
result_f = reader.readtext('images/id_d_f.jpg', detail=0, text_threshold=0.7)
result_b = reader.readtext('images/id_d_b.jpg', detail=0, text_threshold=0.7)
print(f'\nfront side(english)\n {result_f} \n back side(english) \n {result_b}')
