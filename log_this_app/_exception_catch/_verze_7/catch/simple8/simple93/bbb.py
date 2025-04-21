from typing import List, Tuple, Union, Dict
tokens = ('list', '[', 'union', '[', 'int', 'str', ']', ']', '')
type_rules = {
    'list': lambda x: isinstance(x, list),
    'tuple': lambda x: isinstance(x, tuple),
    'union': lambda x, types: any(isinstance(x, t) for t in types),
    'dict': lambda x: isinstance(x, dict),
    'optional': lambda x: x is None or isinstance(x, types[0]),
    'literal': lambda x, literals: x in literals,
    'callable': lambda x: callable(x),
    'sequence': lambda x: isinstance(x, (list, tuple)),
    'int': lambda x: isinstance(x, int),
    'str': lambda x: isinstance(x, str),
    'bool': lambda x: isinstance(x, bool),
    'none': lambda x: x is None
}
def validator(tokens):
    # Načte tokeny a spracovává je po dvou a podle dané dvojice rozhoduje o tom co se má stát.
    # A nebo je načítá po jednom a sekvenčně to řeší - půjdeli
    # Je tedy třeba vymyslet systém a pravidla která by umožnila toto sekvenšní spracování
    # A tedy i jak správně definovat pravidla, zda přes slovník slovníků a nebo přes instance
    # Mohlo by bát výpis co daný prvek všechno očekává a k tomu patřičný úkon - těch věcí co daný prvek umožňuje nebude asi zase tak moc?