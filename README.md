
# 💾 Automação de Backup e Auditoria de Servidores

Projeto em **Python** para automatizar **backups de diretórios críticos**, com **compressão**, **verificação de integridade via SHA256** e **envio de relatórios por e-mail**.

Desenvolvido para ambientes de **Infraestrutura Crítica**, como operações militares, onde a **disponibilidade** e **segurança da informação** são essenciais.

---

## 🚀 Funcionalidades

✅ Backup automático de diretórios especificados.  
✅ Compressão dos arquivos de backup (.zip).  
✅ Geração de **hash (SHA256)** para verificação de integridade.  
✅ Registro de **log de execução**.  
✅ Envio opcional de relatório via **e-mail (SMTP)**.  
✅ Configuração via **arquivo .env** ou **JSON**.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.x**  
- Bibliotecas padrão (`os`, `zipfile`, `hashlib`, `smtplib`, `email`, `json`, `datetime`)

---

## ⚙️ Como usar

1. Clone este repositório:  
```bash
git clone https://github.com/marcelovalebr/backup_auditoria.git
cd backup_auditoria
```

2. Configure o **`config.json`** com os diretórios de origem e destino, além das credenciais de e-mail.

3. Execute o script:  
```bash
python backup.py
```

---

## 📂 Estrutura de Arquivos

```
backup_auditoria/
├── backup.py
├── config.json
├── README.md
└── requirements.txt
```

---

## 🛡️ Aplicações práticas

✅ Garantia de **integridade e segurança de dados** críticos.  
✅ Automatização de processos de **backup e auditoria**.  
✅ Redução de falhas humanas em ambientes de **Infraestrutura Crítica**.  
✅ Utilização em **operações militares**, **indústrias** ou **data centers**.

---

## 👨‍💻 Autor

**Marcelo Vale**  
Especialista em Segurança da Informação | Automação de Processos | Infraestrutura Crítica  

[GitHub](https://github.com/marcelovalebr) | [LinkedIn](https://www.linkedin.com/in/marcelovalebr/)

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo **LICENSE** para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para **forkar** e sugerir melhorias.
