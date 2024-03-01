# is_online

Este projeto consiste em um programa Python que verifica a conectividade de uma lista de endereços IP. Ele envia notificações por e-mail quando um IP fica online ou offline.

## Funcionalidades

- Utiliza a biblioteca ping3 para verificar a conectividade dos IPs.
- Envia e-mails utilizando o protocolo SMTP do Gmail para notificar mudanças de status.
- Trata interrupções de forma adequada para garantir uma finalização limpa do programa.

## Personalização

- As configurações de e-mail e lista de IPs podem ser ajustadas no arquivo '\__main__.py'.
- As mensagens poderão ser modificadas em 'offline.html' e 'online.html'.

## Como usar

1. Clone o repositório.
2. Certifique-se de ter o Docker instalado em seu sistema.
3. Navegue até o diretório do projeto.
4. Execute o comando abaixo para construir e iniciar o contêiner:

```bash
docker-compose up -d
```
