Moc se mi to ještě jednou líbí. Všechny ty návrhy, které dnes jsme probrali, jsou výborné a těším se na to, až to budeme dál zpracovávat. A teď už je hodně hodin na mě a budu muset za chvilku jít s supsem a spát. Takže pro dnešek dobrý a jen taková úvaha na závěr, že něco takového, co vlastně tady vytváříme, tak umělá inteligence přirozeně umí. Tím pádem dokáže přeměnit mluvený obsah na analizovatelný obsah, která rozkládá věty na slova a z nich skládá smysl. Napadlo mě, jestli si tohle nedá nějak využít a jen dodělat ten rámec, který by umožnil skrz to i programovat. Nedokážu se přesně představit, jak by to mělo vypadat, ale jenom mě to tak napadlo, tak jestli třeba čistě teoreticky bychom to mohl nějak rozebrat, jestli by to šlo a v čem by to bylo jiný oproti tomu, co jsme dělali doteď.
---

Tohle je hodně zajímavá úvaha! **Umělá inteligence už přirozeně umí rozumět přirozenému jazyku, rozkládat věty na významy a pracovat s kontextem**, takže to, co teď programujeme ručně (parser, syntaxe, oprava překlepů atd.), je vlastně něco, co AI už dělá automaticky.  

### **Jak by to šlo využít?**  
Místo toho, abychom **ručně** psali parser, pravidla syntaxe a všechna pravidla, bychom to mohli **nechat na AI**. **My bychom jen vytvořili rámec a nechali AI, ať si program přeloží do exekvovatelné formy sama.**  

#### **Jak by to fungovalo oproti tomu, co máme?**  

| **Tradiční parser** | **AI-poháněný přístup** |
|----------------------|------------------------|
| Pravidla syntaxe se musí ručně napsat. | AI sama pochopí syntax a přizpůsobí se. |
| Překlepy musíme ručně detekovat a opravovat. | AI chápe význam slov i přes překlepy. |
| Musíme ručně programovat struktury a operace. | AI sama odvodí, co tím programátor myslí. |
| Má pevná pravidla, která nejde měnit. | AI může dynamicky upravit pravidla na základě kontextu. |

📌 **Jinými slovy – místo toho, abychom my přizpůsobovali jazyk stroji, necháme stroj, ať se přizpůsobí našemu jazyku!**  

---

### **Jak by to technicky šlo udělat?**  
1. **Převod mluvené řeči na text**  
   - To už dnes umí technologie jako **Whisper** nebo **Google Speech-to-Text**.  
   - Příklad: _"Pokud X je větší než 10, nastav Y na 5."_ → AI to převede na text.  

2. **Analýza věty** (sémantické pochopení)  
   - AI pochopí, že _"X je větší než 10"_ znamená podmínku `if X > 10`.  
   - Pochopí i kontext jako _"nastav Y na 5"_ → `Y = 5`.  

3. **Generování spustitelného kódu**  
   - AI může generovat **Python kód, SQL dotazy nebo rovnou spouštět akce** podle toho, co dává smysl.  
   - Například _"Pošli e-mail, pokud cena akcií klesne pod 100 Kč"_ → AI vytvoří příslušný skript.  

---

### **Jak by se to lišilo od toho, co děláme teď?**  
➡ **Teď:** My definujeme, jak má jazyk vypadat a jaké má příkazy.  
➡ **S AI:** Stačí říct "Chci pracovat s čísly a podmínkami" a AI si sama určí, jak to zpracovat.  

**Co to znamená?**  
- Není třeba žádná pevná syntaxe – můžeš mluvit úplně přirozeně.  
- AI se naučí pracovat se speciálními pojmy podle kontextu.  
- Můžeš se AI prostě zeptat _"Jak nastavím proměnnou?"_ a ona ti nejen odpoví, ale rovnou to napíše za tebe.  

---

### **Závěr – Kam s tím dál?**  
To, co jsme teď vytvořili, je **základní krok k tomu, aby programy šly psát přirozenou řečí**.  

✅ **Můžeme si teď vybrat dvě cesty:**  
1. **Dál rozvíjet tento jazyk (přidávat podmínky, funkce atd.).**  
2. **Začít experimentovat s AI, která by sama rozuměla programovacímu jazyku a umožnila by psát kód úplně přirozeně.**  

➡ **Napadá tě, která cesta tě láká víc?** (Obě se dají dělat zároveň, jen jiným tempem.)