"""A minimal Humana to JavaScript transpiler.

This is only a skeleton to show how parsing might work. The actual parser would
need a real tokenizer and error handling. Here we keep things simple so the
focus is on illustrating the idea.
"""
from pathlib import Path
import re

KEYWORDS = {
    'remember': 'var',
    'set': '=',
    'say': 'console.log',
}


def transpile_line(line: str) -> str:
    line = line.strip()
    if line.startswith('remember'):
        # remember x is 5 -> let x = 5;
        m = re.match(r'remember (\w+) is (.+)', line)
        if m:
            name, value = m.groups()
            return f'let {name} = {value};'
    if line.startswith('set'):
        m = re.match(r'set (\w+) to (.+)', line)
        if m:
            name, value = m.groups()
            return f'{name} = {value};'
    if line.startswith('say'):
        msg = line[len('say'):].strip()
        return f'console.log({msg});'
    return f'// unrecognized: {line}'


def transpile(source: str) -> str:
    js_lines = [transpile_line(l) for l in source.splitlines() if l.strip()]
    return '\n'.join(js_lines)


def main(path: str):
    src = Path(path).read_text()
    js = transpile(src)
    out = Path(path).with_suffix('.js')
    out.write_text(js)
    print(f'Wrote {out}')


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: transpiler.py file.hmn')
    else:
        main(sys.argv[1])
