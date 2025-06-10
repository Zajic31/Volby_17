# Volby_17

Dobrý den, moje jméno je David Vangárd a jmenuji se David Vangárd a mám tady tenhle Python projekt a dnes vám ukážu co s ním všchno umím...</bl>

Moje upřímná reakce po tom co nemám za 5 (snad): <img src="https://t4.ftcdn.net/jpg/02/25/43/37/360_F_225433780_adJUNaMFOgZDEY2lELYXAqfj4jCX7dBX.jpg">

<h2><b>Co je to za projekt?</b></h2>
    <p>
        Tento kód získává výsledky voleb do pralamentu v roce 2017 napříč ČR - <a target="_blank" href="https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ">web zde</a> - (musíte vybrat konkrétní okres ve sloupcích) a následně je zapíše do CSV souboruů. 
    </p>
    
<h2><b>How to spustit</b></h2>
    <p>
        Před spuštěním samotného skriptu si musíte stáhnout potřebné knihovny uvedené v souboru <a href="https://github.com/Zajic31/Volby_17/blob/main/requirements.txt"> requirements.txt</a>. Samotný kód následně spustíte z Terminálu pomocí tohoto příkazu:</p><bl> 
        <ul>python projekt_3.py "odkaz-okresu" "nazev-vystupniho-souboru.csv"</ul>
    </p>
    <p>
        Následný výstup bude .csv soubor s výsledky pro vybraný okres :3
    </p>

<h2><b>Praxe</b></h2>
    <p>
        Např. pro okres Nymburk </bl> 
        <ol>
            <li>
                Odkaz: <a href="https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108">https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108</a>
            </li>
            <li>
                Nazev výstupního souboru: vysledky_nymburk.csv
            </li>
            <li>
                Spouštění skriptu: </bl>
                python projekt_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108" vysledky_kolin.csv
            </li>
            <li>
                Začne probíhat průběh programu
            </li>
            <li>
                Následný výstup bude: <a href="https://github.com/Zajic31/Volby_17/blob/main/vysledky_nymburk.csv">vysledky_nymburk.csv</a>
            </li>
        </ol>
    </p>

<h2>HOTOVSON</h2>
    <img src="https://ih1.redbubble.net/image.490263180.2295/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg">
