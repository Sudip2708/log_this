To dává smysl a líbí se mi ten přístup, že binární vrstva je optimalizovaná na co nejstručnější reprezentaci základních operací. Pokud chápu správně, principy jazyka by byly následující:  

1. **Všechno je objekt**  
   - Třídy, funkce, podmínky, cykly i proměnné jsou objekty.  
   - Funkce i třída jsou vlastně totéž, rozdíl je jen v tom, jak se používají.  
   - To znamená, že dědičnost může fungovat jak pro třídy, tak pro funkce.  

2. **Binární vrstva s optimalizovanými instrukcemi**  
   - Místo tradičního přenosu po bytech se pracuje s kratšími sekvencemi.  
   - Základní operace (např. podmínky, cykly) mají co nejkratší binární reprezentaci.  
   - To by umožnilo extrémně efektivní interpretaci na úrovni procesoru.  

3. **Lidsky čitelná vrstva nad binární vrstvou**  
   - Uživatel pracuje s kódem v přirozené podobě (např. `pokud (x > 5), dělej (něco)` nebo `if x is greater than 5, then do something`).  
   - Syntaxe je flexibilní, může být čitelná i v různých jazycích.  
   - Překladač/interpret překládá tento zápis na optimalizovanou binární podobu.  

To sjednocení funkcí a tříd do jednoho objektového systému **mi přijde jako správný krok**, protože pokud všechno je objekt, pak není důvod rozlišovat mezi funkcemi a třídami. Vlastně i v Pythonu nebo JavaScriptu se funkce chovají jako objekty (mohou mít atributy, mohou být uloženy do proměnné).  

Co se mi na tom líbí:  
✅ **Jednoduchost konceptu** – všechno je objekt, takže není potřeba dělat rozdíly mezi datovými typy, funkcemi a třídami.  
✅ **Optimalizace na binární úrovni** – efektivní zpracování základních operací.  
✅ **Lidsky čitelná syntaxe** – přirozenější zápis kódu.  

Co bude potřeba promyslet:  
❓ **Jak bude vypadat binární kód pro složitější struktury?** – např. jak se uloží podmínky, jak se reprezentují složené objekty.  
❓ **Jak bude fungovat dědičnost?** – pokud funkce i třídy dědí, bude potřeba určit, jak se rozlišují instance a prototypy.  
❓ **Jak se budou volat objekty?** – bude rozdíl mezi `objekt()` a `objekt.něco()` nebo to bude sjednocené?  

Kam chceš jít dál? Chceš se zaměřit na konkrétní část, třeba jak definovat objekty v binární vrstvě?