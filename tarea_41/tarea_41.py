import re
from collections import defaultdict

initial_text = """En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
                    referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
                    Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
                    olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
                    hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
                    ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
                    Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
                    increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
                    quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
                    porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
                    solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
                    yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
                    El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
                    congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
                    semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
                    Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
                    hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
                    se encarga de pensar, y hasta cantamos juntos la canción de Annie.
                    Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
                    Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."""

# This way we can easily test our code with another string, without needing to modify the lines below.
str_under_test = initial_text

# Define the regexp parsers
# For chars
char_parser = re.compile(".")
# For words
word_parser = re.compile("\w+")

# Now we get the list of all the chars and all the words.
chars = char_parser.findall(str_under_test)
words = word_parser.findall(str_under_test)
# In order to count how many times a certain word appears, we will iterate through the word list and increment its value
# in a dictionary per each apparition.
histogram = defaultdict(int)
for word in words:
    histogram[word] += 1

# Finally we display the results.
print("Amount of chars: {}".format(len(chars)))
print("Amount of words: {}".format(len(words)))
print(["{}: {}".format(key, value) for key, value in sorted(histogram.items(), key=lambda x: x[1], reverse=True)])

# More efficient implementation. The previous one used findall, which creates a list instead of an iterator (iterators are more memory efficient).
# For that reason we will try to implement the same code useing iterators.

chars_it = char_parser.finditer(str_under_test)
words_it = word_parser.finditer(str_under_test)

char_amount = sum(1 for element in chars_it)

word_amount = 0
histogram = defaultdict(int)
for word in words_it:
    # This is neccessary to get the string from the match object.
    word = word.group(0)
    word_amount += 1
    histogram[word] += 1

# Finally we display the results.
print("Amount of chars: {}".format(len(chars)))
print("Amount of words: {}".format(len(words)))
print(["{}: {}".format(key, value) for key, value in sorted(histogram.items(), key=lambda x: x[1], reverse=True)])

