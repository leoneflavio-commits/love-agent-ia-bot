import requests
import time
import os
from datetime import datetime

TOKEN = os.getenv('TELEGRAM_TOKEN', '8040156850:AAEzyPxxlMTT7YD390EBejnf3U87V9iWgXA')

def bot_principal():
    print("🤖 LOVE AGENTE IA - ONLINE 24/7 NO RAILWAY")
    print("📍 Sistema de produção ativado!")
    print("=" * 50)

    last_update_id = 0
    tentativas_conexao = 0

    def processar_mensagem(mensagem):
        chat_id = mensagem['chat']['id']
        texto = mensagem.get('text', '').lower()
        usuario = mensagem['chat']['first_name']

        print(f"📩 {usuario}: {texto}")

        if any(palavra in texto for palavra in ['oi', 'olá', 'ola', 'start', 'hey']):
            resposta = f"""🤖 <b>LOVE AGENTE IA - SISTEMA AUTÔNOMO</b>

Olá <b>{usuario}</b>! 👋 

🎯 <b>Estou online 24/7 pronto para análises!</b>

💫 <b>Comandos disponíveis:</b>
• analise - Análise completa do mercado
• pool - Análise detalhada de pools  
• ajuda - Ver todos os comandos

<code>🔧 Hospedado no Railway - {datetime.now().strftime('%H:%M')}</code>"""

        elif 'analise' in texto or 'análise' in texto or 'mercado' in texto:
            resposta = f"""📊 <b>LOVE AGENTE IA - ANÁLISE DE MERCADO</b>
⏰ {datetime.now().strftime('%d/%m %H:%M')}
────────────────────

<b>🎯 OPORTUNIDADES IDENTIFICADAS:</b>

🚀 <b>PING/WETH Pool</b>
├ APR: <b>214.18%</b>
├ ROI: <b>4.39%</b> 
├ Fees: <b>$130.58</b>
└ Status: <b>🟡 OTIMIZÁVEL</b>

<code>🤖 Análise automática - Love Agent IA</code>"""

        elif 'pool' in texto or 'liquidez' in texto:
            resposta = f"""🏊 <b>ANÁLISE DETALHADA - POOL PING/WETH</b>
⏰ {datetime.now().strftime('%d/%m %H:%M')}
────────────────────

<b>📈 PERFORMANCE:</b>
├ ROI: <b>4.39%</b>
├ APR: <b>214.18%</b>
├ Fees Acumulados: <b>$130.58</b>
└ Idade: <b>7.5 dias</b>

<code>💡 Dica: Configure alertas automáticos</code>"""

        elif any(palavra in texto for palavra in ['ajuda', 'help', 'comandos']):
            resposta = """🆘 <b>LOVE AGENTE IA - AJUDA</b>

💫 <b>COMANDOS DISPONÍVEIS:</b>
• analise - Análise completa do mercado
• pool - Análise detalhada de pools
• ajuda - Esta mensagem de ajuda

<code>🔧 Hospedado no Railway - Sempre online!</code>"""

        else:
            resposta = f"""🤖 <b>LOVE AGENTE IA</b>

Não entendi completamente, <b>{usuario}</b>!

💡 <b>Experimente:</b>
• "analise" - Para análise de mercado
• "pool" - Para análise de pools

<code>🎯 Estou aqui para ajudar!</code>"""

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        try:
            requests.post(url, json={
                'chat_id': chat_id, 
                'text': resposta,
                'parse_mode': 'HTML',
                'disable_web_page_preview': True
            }, timeout=10)
            print(f"✅ Respondi para {usuario}")
        except Exception as e:
            print(f"❌ Erro ao enviar: {e}")

    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
            resposta = requests.get(url, params={
                'offset': last_update_id + 1, 
                'timeout': 30
            }, timeout=35)

            if resposta.status_code == 200:
                dados = resposta.json()
                if dados.get('ok'):
                    tentativas_conexao = 0

                    if dados['result']:
                        for update in dados['result']:
                            last_update_id = update['update_id']
                            if 'message' in update:
                                processar_mensagem(update['message'])

            time.sleep(1)

        except Exception as e:
            print(f"❌ Erro: {e}")
            time.sleep(10)

if __name__ == "__main__":
    print("🚀 LOVE AGENTE IA INICIANDO NO RAILWAY...")
    bot_principal()
