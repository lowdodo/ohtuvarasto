from varasto import Varasto

def main():
    mehua, olutta = Varasto(100.0), Varasto(100.0, 20.2)
    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}\n"
          f"Olut getterit:\nsaldo = {olutta.saldo}\n"
          f"tilavuus = {olutta.tilavuus}\n"
          f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n"
          f"\nMehu setterit:\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}\n\nVirhetilanteita:\nVarasto(-100.0);")
    print(f"{Varasto(-100.0)}\nVarasto(100.0, -50.7)\n{Varasto(100.0, -50.7)}")
    olutta.lisaa_varastoon(1000.0)
    print(f"\nOlutvarasto: {olutta}\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"Mehuvarasto: {mehua}\nolutta.ota_varastosta(1000.0)\n"
          f"saatiin {saatiin}\nOlutvarasto: {olutta}")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\nMehuvarasto: {mehua}")

if __name__ == "__main__":
    main()
