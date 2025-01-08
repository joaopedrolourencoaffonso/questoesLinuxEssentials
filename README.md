# Linux Essentials Test Questions Repository

![Linux Essentials](https://img.shields.io/badge/Linux-Essentials-orange)
![Questões](https://img.shields.io/badge/Questions-100%2B-brightgreen)

Este repositório é dedicado a fornecer uma coleção abrangente de questões de teste do Linux Essentials para aprender e praticar os fundamentos do Linux. Seja você um iniciante procurando explorar o mundo do Linux ou um usuário experiente querendo aprimorar suas habilidades, este repositório é para você!

As questões estão disponíveis para estudo de duas maneiras:
- [Em formato de questionário interativo online](https://joaopedrolourencoaffonso.github.io/questoesLinuxEssentials/)
- [Em formato JSON para fácil importação e uso local](./static/questoes.json)

## Executando localmente

Caso deseje executar esse projeto localmente, comece clonando o presente repositório:

```bash
$ git clone https://github.com/joaopedrolourencoaffonso/questoesLinuxEssentials.git
```

Acesse o repositório e instale as dependências:

```bash
$ cd questoesLinuxEssentials
$ pip install -r requirements.txt
```

Por fim, aplique o comando:

```bash
$ python ./app.py
```

A aplicação estará disponível em http://127.0.0.1:5000

Para encerrar, basta usar o ctrl + C.

# Metas
- [X] Mais de 100 questões de múltipla escolha em arquivo json para fácil importação
- [X] Respostas
- [X] [Site para praticar](https://joaopedrolourencoaffonso.github.io/questoesLinuxEssentials/)

## Contribuindo

Se você deseja contribuir para o projeto, fique à vontade para abrir uma *issue* ou enviar um *pull request* com melhorias ou novas questões.

1. Fork este repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-branch`).
3. Comite suas mudanças (`git commit -am 'Adicionando novas questões'`).
4. Envie a branch (`git push origin minha-branch`).
5. Abra uma *pull request* para revisão.

Todos os estudantes de Linux agradecem sua contribuição!