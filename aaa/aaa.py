def speed_up(current_speed):
    if current_speed:
        print(current_speed + 10)
    else:
        print("Current speed was not specified.")

"""
Ahojky :-)

Mohl bys mi zkusit vytvořit nějaký jednoduchý navr pro asembler který obdrží řetězec, který nejprve roztřídí na věty (dle tečky s mezerou za ní), dále pak věty které jsou interní rozdělí na souvětí (dle čárky a mezery za ní). Toto rozdělení souvět by tak mělo být vnořené do objektu věty.
A následně větu rozdělí na slova (dle mezry mezi nimi).
A v posledním kroku vezme popořadě věty a každé slovo se pokusí vyhledat ve slovníku object, kde je pro každé slovo definovaný nějaký úkon, který následně provede.

Ve finále bych měl dostat assembler, který by mi dokázal rozebrat tuto větu:

Create object speed up. Object speed up expect value current speed. Object speed up print value current speed plus ten, if value current speed, else print text current speed was not specified.

Která by mohla být zapsaná i takto:

Create object speed up. 
Object speed up expect value current speed. 
Object speed up print value current speed plus ten, 
    if value current speed, 
    else print text current speed was not specified.

A která by byla rozebrána na jednotlivá slova a pak k těm slovům by byl dohledáván význam, který by měli reprezentovat.

Takže například:

Create object = vytvoř objekt (za tímto souslovím následuje zadání jména objektu ukončeného tečkou, nebo při diktování souslovím end dot)
speed up. = Řetězec reprezentující jméno objektu (tečka určuje konec řetězce)
Zde se sluší asi i vysvětlit co se snažím dosáhnout. Snažím se představit si jak by mohl vypadat jazyk, který by byl založen na přirozené řeči, takže kromě zkrácených forem zápisu, by umožňoval zápis skrze dktování slov.
Takže po získání této první věty:
Create object speed up.
By došlo j jejímu rozboru na jednotlivá slova (malímy písmeny - vlké písmenu na začátku věti je jen estetickou zležitostí pr snažší orientaci a zachování přirozené mluvnice):
["create", "object", "speed", "up"]
Po té by se snažil vyhledat v předefinovaných objektech slovo "create",
Zde by zjistil že slovo "create" je zde uvedeno ve více variantách a tak by použil i druhé slovo "object",
Zde by už zjistil že slovní spojení ("create", "object", nebo "create_object") je zde pouze jediné takže by sekoukl, na jaký objekt tato klíčová slova odkazují.
A zjistil by že tato formulace říká: Vytvoř funkci a jako další parametr, a to až do tečky, bude definice jména funkce.
Takže by vzal zbylá slova "speed", "up" a vytvořil by z nich název funkce "speed_up".
A rovou by tedy založil objekt "speed_up" nebo ("speed", "up") - formu ještě přesně nevím - a uložil ho do registru objektů.
A ten objekt by v tuto chvíli vypadal takto:
def speed_up:
    pass
    
A samotná struktura objektu by v tuto chvíli vypadala nějak takto:
objects = {
    speed_up: {
        "name": ("speed", "up")
    }
}

Následně by začal spracovávat další větu:
["object", "speed", "up", "expect", "value", "current", "speed"]
Zde by tedy bylo první slovo "object", které pokud by bylo psané bez upřesnění akce před tímto slovem, jako například v minulé větě bylo slovo "create", pak by dohledal objekt který odkazuje na toto slovo.
Zde by zjistil že toto slovo značí, že za ním bude následovat název jiného objektu, který je již vytovřený.
Takže by nejprve vzal další slovo v řadě "speed" a podíval se do seznamu objektů a zjistil že je zde jeden výraz ("speed", "up"), který slovo "speed" obsahuje.
Dále by zjistil, že toto slovo vyžaduje další slovo "up", tak aby se mohl vrátit daný objekt.
Takže se vrátí k textu a podívá se jestli další sovo je zde uvedené.
To by tedy našel, takže by z této věty už měl tři slova zpracovaný:
"object", "speed", "up"
Která by znamenala načti objekt "speed_up".

Dálším slovem je "expect", které je objektem který specifikuje co objekt vyžaduje pro svoji funkčnost a zároveň by zjistil, že toto slovo potřebuje ještě upřesnění, protože je zde zase ve více variantách.
Podíval by se tedy na další slovo a zjistil, že je jím "value", které dohromady ve slovním spojení ("expect", "value") znamená že objekt pro svojí funkci vyžaduje nějakou číselnou hodnotu.
A zároveň by věděl, že po tomto slovním spojení až do konce věty bude následovat pojmenování této hodnoty.
Načetl by tedy zbylá slova: "current", "speed" a vytvořil z nich jméno nového objektu "current_speed" který by byl deklarací že objekt v kterém je použit očekává určitou číselnou hodnotu.
A tento objekt by se tedy uložil pod objekt "speed_up" na kterém byl definován.
Takže náš objekt by v tu chvíli již vypadal takto:
def speed_up(current_speed: int, float):
    pass
    
A samotná struktura objektu by v tuto chvíli vypadala nějak takto:
objects = {
    "speed_up": {
        "name": ("speed", "up"),
        "expect": {
            "current_speed": {
                "name": ("current", "speed"),
                "type": (int, float) # toto by specifikovalo právě zadání slova "value", který by bylo odkazem specifikující že jde o číselnou hodnotu
            }
        }
    }
}

Tím by byla druhá věta hotová a následně by se pustil podobně do třetí věty, která je souvětím, takže by byla spracovávaná jako celek, kde každá čárka by oddělovala určitou logiku.
Zde už asi není potřeba znovu popisovat clý proces, ten by byl prakticky pořád stejný.
A výsledkem rozebrání této věty by měla být tato logika:
    if current_speed:
        print(current_speed + 10)
    else:
        print("Current speed was not specified.")
        
Takže v konečném důsledku, po zadání těchto vět by se měl vytvořit objekt "speed_up", který by obsahoval tuto logiku:
def speed_up(current_speed: int, float):
    if current_speed:
        print(current_speed + 10)
    else:
        print("Current speed was not specified.")
        
Z víše zmíněného je už asi jasné kam s tím mířím, že bych si rád pro sebe zkusil vytvořit nadstavbu nad jazykem Python, která by umožňovala vytvářet kod pouhou řečí.
Ještě to tedy nemám celé pořádně promyšlené, ale tady je tedy pár poznatkům, ke kterým jsem si při přemýšlení o tom došel:
1) V této nadstavbě by vše bylo vnímané jako jednotný objekt, kde jeho vnitřní parametry by rozhodovali o tom jak se bude chovat.
Jednalo by se tedy o deklarativní jazyk, který by měl předefinované veškeré výpočetní operace, cykli, podmínky, atd, a to právě formou interních objektů, které by všechny drželi stejnou formu a byli by zapsatelné taktov ve slovníku s vnořenými slovníky.
Tato jednotnost by pak umožnila snadnější zadávání, protože tím, že se jedná o deklarativí jazyk, vždy by muselo být uvedeno co s čím se má stát a interpretr by ak jen zjistil, zda je to možné, a úkon provedl a kdyby to možné nebylo vyvolal by výjimku.

2) Základem je pak vtváření vlatních objektů, které by mohl plnit nejrůznější funkce, od objektu, který by reprezentoval jen přiřazení proměné, přes funkce až po delkarace tříd.
Toto vše by se dělo na základě vnitřních objektů, které by zpracovávaný objekt obsahoval.
S tím že do budoucna počítám s určitou optymalizací, která by objekty s jednoduchou strukturou (třeba jen s jednou vloženou funkcí jako je zde "current_speed" která je potomek objektu "value" a tím pádem jde o deklaraci proměné s očekávanými typy pro číselné operace),
zpracovával jiným způsobem než složitější objety - ale ve finále složitost sprácování by byla úměrná k složitosti objektu.
Takže uživatel by mohl deklarovat vlastní objekty a k tomuto by sloužilo slovní spojení ("create", "object").

3) Každá věta by byla uzavřeným příkazem a pokud by příkaz obsahoval složitější logiku, jako je v načem případu podmínka, pak by se jednotlivé části oddělovali čárkou.
Takže souvětí by znamenala širší logiku a ta by zase byla zpracovávaná na základě slov a slovních spojení, které by odkazovali na vnitřní objekty (a nebo i vytvořené, jako je "Object speed up").
Tyto vnitřní objekty ba tak již v sobě obsahovali předefinovanou logiku, která by třeba pro objekt který odkazuje na "print" by věděl že do konce věty (tečka nebo čárka) následuje řetězec který se má uložit jako objekt text a který se má vytisknout.
A když taková věta nekončí tečkou, ale pokračuje čárkou, pak by se příkaz ještě neprovedl, ale věta by se četla dál a došlo by se na další klíčové slovo "if", které by bylo objektem pro spracování podmínky.
Takže by se došlo k slovu "if", které by značilo že následuje podmínka:  "value current speed", která by říkala že má být zadané číslo pro objekt "current speed".
Který by tedy po své deklaraci (Object speed up expect value current speed.) už existoval v paměti vytvořených objektů pro objekt "speed up" a mohlo se na něja takto přímo odkazovat.
Kdyby za touto větou byla tečka, pak by tato podmínka vypadala takto:
    if current_speed:
        print(current_speed + 10)
        
Ale tím, že věta dále pokračuje čárkou, je jasné že bude následovat další upřesnění, které tedy začíná slovem "else", které je samo objektem uvnitř objektu "if" a jeli použito vytváří se větev else.
A za ním je znovu "print" za kterým až do konce věty následuje řetězec pro vytištění.

Všechno toto by se pak uložilo do původního objektu:

objects = {
    "speed_up": {
        "name": ("speed", "up"),
        "expect": {
            "current_speed": {
                "name": ("current", "speed"),
                "type": (int, float) # toto by specifikovalo právě zadání slova "value", který by bylo odkazem specifikující že jde o číselnou hodnotu
            },
        },
        "return": {
            "condition": {
                "if": {
                    "condition": "current_speed",
                    "result": {
                        "print": {
                            "compile": {
                                "addition": {
                                    "firs_value": "current_speed",
                                    "second_value": 10
                                }
                            }
                        }
                    }
                },
                "else": {
                    "result": {
                        "print": {
                            "text": "Current speed was not specified."
                            }
                        }
                    }
                }
            }
        }
    }
    
Tím by se vytvořil objekt "speed_up" obsahující logiku pro to by se choval jako funkce.

S tím, že zatím si vše dávám jen v hlavě dohromady, takže si nejsem plně jistý jak toto uchopit.
Nicméně toto mám jako odrazový můstek a to co mě napadlo, že vlastně jako první potřebuji nástroj, který by nejen byl schopný takto zobjektivizovat zadanou větu, ale i umožnoval správu objektů.

Co ty na to?
Hlavní myšlenka je, že kdo umí mluvit umí i programovat a snaha přiblíži programování i lidem, kteří si myslí, že pro programování jsou potřeba naučit se nejprve složitou synaxi skládající se často z skratek, kterým lidé nerozumí a tak mohou vnímat programování jako něco velmi složité0.
Tímto projektem se tedy zatím spíše bavím a zkouším hledat cesty jak by se toho dalo dosáhnout :-)

"""
