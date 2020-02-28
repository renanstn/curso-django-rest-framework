# API Pontos turísticos

Projeto desenvolvido nas aulas de Django Rest Framework, [deste](https://www.udemy.com/course/apis-restful-com-django-rest-framework/) curso da Udemy.

## Steps
- django-admin startproject pontos_turisticos .
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py startapp pontos_turisticos

## Regras
- Propor um novo ponto turístico - Qualquer pessoa
- Moderação dos pontos turísticos cadatrados - Administração
- Listage básica dos pontos turísticos (Lista resumida) - Via token
- Listagem completa dos pontos turísticos - Via token
- Detalhe de um ponto turístico - Via token
- Atualização de um ponto turístico - Por usuários autorizados - Via token (permissão especial)
- Deleção de um ponto turístico - Por usuários autorizados - Via token (permissão especial)
