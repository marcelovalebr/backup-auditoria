import os
import zipfile
import hashlib
import smtplib
import json
from datetime import datetime
from email.message import EmailMessage

def carregar_config():
    with open('config.json') as f:
        return json.load(f)

def criar_backup(diretorio, destino):
    nome_backup = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    caminho_backup = os.path.join(destino, nome_backup)
    
    with zipfile.ZipFile(caminho_backup, 'w') as zipf:
        for root, _, files in os.walk(diretorio):
            for file in files:
                full_path = os.path.join(root, file)
                zipf.write(full_path, os.path.relpath(full_path, diretorio))
    
    return caminho_backup

def gerar_hash(caminho_arquivo):
    sha256 = hashlib.sha256()
    with open(caminho_arquivo, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b''):
            sha256.update(bloco)
    return sha256.hexdigest()

def enviar_email(relatorio, config):
    msg = EmailMessage()
    msg['Subject'] = 'Relatório de Backup e Auditoria'
    msg['From'] = config['email_usuario']
    msg['To'] = config['email_destinatario']
    msg.set_content(relatorio)

    with smtplib.SMTP_SSL(config['email_servidor'], config['email_porta']) as smtp:
        smtp.login(config['email_usuario'], config['email_senha'])
        smtp.send_message(msg)

def main():
    config = carregar_config()
    diretorio = config['diretorio_backup']
    destino = config['destino_backup']
    
    caminho_backup = criar_backup(diretorio, destino)
    hash_backup = gerar_hash(caminho_backup)
    
    log = f"""
Backup realizado com sucesso!
Arquivo: {caminho_backup}
Hash SHA256: {hash_backup}
Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    print(log)
    
    with open(os.path.join(destino, 'log_backup.txt'), 'a') as f:
        f.write(log + "\n")
    
    if config.get('email_notificacao'):
        enviar_email(log, config)

if __name__ == '__main__':
    main()
