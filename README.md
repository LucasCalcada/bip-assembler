# BIP Assembler
## Introdução
O projeto se trata de um assemblador desenvolvido para o projeto semestral da disciplina "ECM245 - Arquitetura e Organização de Computadores".

Esse assemblador converte o código em linguagem de máquina que pode ser interpretada pelo processador BIP desenvolvido em aula.
## Como funciona
Primeiramente, define-se o conjunto de instruções através do arquivo `config.yaml`
```yaml
instructions:
  - name: OUT
    address: 0
    constParam: false
    addressParam: true
    tagParam: false

  - name: IN
    address: 1
    constParam: false
    addressParam: true
    tagParam: false

  - name: JG
    address: 2
    constParam: true
    addressParam: false
    tagParam: true
# ...
```
Depois, basta executar o arquivo `main.py` passando o nome do arquivo com o código como parâmetro
```
python main.py <nome do arquivo>
```
O arquivo final será criado no mesmo diretório com o nome `output.cdl`
## Recursos
O assemblador oferece algumas funcionalidades como:
* Uso de comentários
* Criação de "tags" para serem referenciados pelas instruções de `JUMP`
