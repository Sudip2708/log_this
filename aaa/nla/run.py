# Příklad použití
from natural_language_assembler import NaturalLanguageAssembler

if __name__ == "__main__":
    assembler = NaturalLanguageAssembler()

    test_text = """
    Create object speed up. 
    Object speed up expect value current speed. 
    Object speed up print value current speed plus ten, 
    if value current speed, 
    else print text current speed was not specified.
    """

    result = assembler.compile(test_text)
    print("Parsed result:", result)

    python_code = assembler.generate_python()
    print("\nGenerated Python code:")
    print(python_code)