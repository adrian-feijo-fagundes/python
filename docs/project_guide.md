Se você quer o **básico mesmo**, para começar um projeto Python do zero, eu usaria este fluxo:

### 1. Criar a pasta do projeto

```bash
mkdir meu_projeto
cd meu_projeto
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

Ativar:

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

Depois disso, o terminal normalmente mostra algo como:

```text
(.venv) ...
```

### 3. Criar o arquivo principal

Linux/macOS:

```bash
touch main.py
```

Windows:

```powershell
New-Item main.py
```

Estrutura inicial:

```text
meu_projeto/
├── .venv/
└── main.py
```

### 4. Testar

No `main.py`:

```python
print("Olá, mundo!")
```

Executar:

```bash
python main.py
```

---

### 5. Se precisar instalar bibliotecas

Com o ambiente virtual ativado:

```bash
pip install nome-da-biblioteca
```

Por exemplo:

```bash
pip install requests
```

E para registrar as dependências:

```bash
pip freeze > requirements.txt
```

Depois, em outro computador:

```bash
pip install -r requirements.txt
```

---

### 6. Git, se quiser versionar

```bash
git init
```

Criar `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
```

Depois:

```bash
git add .
git commit -m "projeto inicial"
```

### O conjunto que vale decorar

Para projetos pequenos, eu diria que estes são os principais:

```bash
mkdir projeto
cd projeto

python -m venv .venv

# ativar ambiente virtual

python main.py
pip install biblioteca
pip freeze > requirements.txt

git init
```

E uma coisa importante: **você não precisa criar uma estrutura gigante de pastas para todo projeto Python**. Para aqueles seus projetinhos de um dia, como o organizador de arquivos ou um projeto simples com SQLite, `main.py + .venv` já é perfeitamente suficiente.
