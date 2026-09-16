import sympy as sp

# 1. Määritetään matemaattiset symbolit ja vakio (Golden Ratio phi)
# Käytetään symbolista laskentaa, jotta sqrt(5) pysyy täysin tarkkana algebrallisena oliona
sqrt5 = sp.sqrt(5)
phi = (1 + sqrt5) / 2

print("--- 1. PARADIGMAN ALUSTUS ---")
print(f"Kultainen leikkaus phi symbolisena: {phi}")

# 2. Alkuperäinen signaali S_input kuuluu rationaalilukuihin Q
# Valitaan esimerkkisignaaliksi rationaaliluku, esim. S_input = 42
S_input = sp.Rational(42, 1)
print(f"Alkuperäinen signaali (S_input): {S_input}  (Kuuluu kuntaan Q)")

# 3. Lähetyspuolen koodaus (Transmitter-Side Embedding)
# Skaalataan signaali phi^3:lla, jolloin se siirtyy kuntaan Q(sqrt(5))
# Kaava: S_modulated = S_input * phi^3
S_modulated = S_input * (phi ** 3)
print(f"Skaalattu signaali (S_modulated): {S_modulated.simplify()}  (Kuuluu kuntaan Q(sqrt(5)))")

# 4. Kanavakohina (Transcendental Channel Noise)
# Luodaan kohina, joka EI kuulu kuntaan Q(sqrt(5)), esimerkiksi pii (pi) tai e
# Tämä edustaa dokumentin transsendenttista häiriömuuttujaa N(t)
noise = sp.pi / 10
print(f"Transsendenttinen kohina (N): {noise}  (EI kuulu kuntaan Q(sqrt(5)))")

# Vastaanotettu signaali kanavasta (Channel Topology)
S_transmitted = S_modulated + noise
print(f"Vastaanotettu signaali (S_transmitted): {S_transmitted}")

print("\n--- 2. VASTAANOTTO JA KOHINAN EROTTAMINEN (MS-GD-ERS) ---")

# 5. Algebrallinen suodatus / Entrooppinen tunnistus
# Koska tiedämme, että alkuperäinen payload koostuu VAIN muotoa a + b*sqrt(5) olevista luvuista,
# voimme tunnistaa transsendenttisen osan (pii), joka rikkoo tämän algebrallisen rakenteen.
# Laajennetaan lauseke auki:
expanded_signal = S_transmitted.expand()

# Erotetaan algebrallinen kanta ja transsendenttinen jäännös (kohina)
# Täydellinen palaute- ja vaimennusluuppi tunnistaa osat, jotka eivät ole muotoa Q + Q*sqrt(5)
algebraic_part = 0
transcendental_part = 0

# Käydään läpi vastaanotetun signaalin komponentit
for term in sp.Add.make_args(expanded_signal):
    # Jos termi sisältää piin (transsendenttisen kohinan), ohjataan se "lämpöhukaksi"
    if term.has(sp.pi):
        transcendental_part += term
    else:
        algebraic_part += term

print(f"Bannattu/Erotettu kohina (Lämpöhukka / Dissipation): {transcendental_part}")
print(f"Puhdistettu algebrallinen payload: {algebraic_part.simplify()}")

print("\n--- 3. LOPPUTULOKSEN SYNTEESI ---")

# 6. Täydellinen signaalin palautus käänteisoperaattorilla phi^-3
# Kaava: S_output = algebraic_part * phi^-3
S_output = algebraic_part * (phi ** -3)
S_output_final = S_output.simplify()

print(f"Lopullinen purettu signaali (S_output): {S_output_final}")
print(f"Onko synteesi täydellinen (S_output == S_input)? -> {S_output_final == S_input}")
