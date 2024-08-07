# Dáma

Dáma je klasická desková hra, kterou jsme implementovali v Pythonu pomocí knihovny Pygame. Tato verze obsahuje AI soupeře a podporuje všechna standardní pravidla hry.

## Funkce

- **Jednoduchá AI**: Zahrajte si proti počítači s různými úrovněmi obtížnosti.
- **Vícenásobné skákání**: Podpora pro vícenásobné skákání podle pravidel dámy.
- **Proměna v krále**: Figurky se promění v krále, když dosáhnou poslední řady soupeře.
- **Povinné skákání**: Hráči musí skákat, pokud mají možnost.
- **Animace pohybu**: Plynulé animace pohybu figur.

## Instalace

1. Klonujte tento repozitář:
    ```bash
    git clone https://github.com/Montikks/Dama.git
    ```
2. Přejděte do adresáře projektu:
    ```bash
    cd Dama
    ```
3. Vytvořte virtuální prostředí a aktivujte ho:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Na Windows
    source .venv/bin/activate  # Na macOS/Linux
    ```
4. Nainstalujte závislosti:
    ```bash
    pip install -r requirements.txt
    ```

## Použití

1. Spusťte hlavní skript:
    ```bash
    python main.py
    ```
2. V hlavním menu si můžete vybrat úroveň obtížnosti AI a začít novou hru.

## Pravidla hry

- Hráči se střídají v tazích.
- Pohyb je možný pouze diagonálně.
- Pokud má hráč možnost skákat soupeřovy figurky, musí to udělat.
- Vícenásobné skákání je povoleno.
- Když figurka dosáhne poslední řady na soupeřově straně, stane se králem a může se pohybovat i dozadu.
- Hra končí, když jeden z hráčů nemá žádné figurky nebo platné tahy.

## Přispívání

Přispěvatelé jsou vítáni! Pokud máte zájem o přispívání, prosím, postupujte podle těchto kroků:

1. Forkněte tento repozitář.
2. Vytvořte novou větev (`git checkout -b feature/nova-funkce`).
3. Proveďte změny a commitujte (`git commit -am 'Přidání nové funkce'`).
4. Pushněte větev (`git push origin feature/nova-funkce`).
5. Vytvořte nový Pull Request.

## Licence

Tento projekt je licencován pod licencí MIT. Podrobnosti naleznete v souboru [LICENSE](LICENSE).

## Kontakty

- **Autor:** Montikks
- **Email:** Monty.01@seznam.cz
