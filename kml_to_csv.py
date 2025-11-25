import sys

def parse(content, key_words):
    tokens=list()
    token=""
    label=False
    name=False 
    for c in content:
        if (c=='<'):
            label = True 
            if name: 
                tokens.append(token)
                name=False
            continue
    
        if (c=='>'):
            label = False
            if token in key_words: 
                tokens.append(token)
                name=True
            token=""
            continue
    
        if (label or name):
            token = token + c

    return tokens

def main(argv: list[str]) -> int:
    with open("Capitales de europa.kml") as file:
        content=file.read()
   
    key_words = argv[1:]
    tokens = parse(content, key_words)

    with open("capitales_europa.csv", "w", encoding="utf-8") as csv:
        csv.write(",".join(key_words) + "\n")

        out=False
        count=0
        line=list()
        for token in tokens:
            if token in key_words: 
                out = not out
                continue
            if out: 
                line.append(token)
                count = count + 1
            if count == len(key_words):
                count = 0
                csv.write(",".join(line) + "\n")
                line.clear()

    return  0;
    

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
