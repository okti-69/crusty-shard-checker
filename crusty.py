# Takie info:
# Nie jestem jakis py master wiec to jest glupio zrobione xD wazne ze dziala
id_webhooka = "TU ID WEBHOOKA"
token_webhooka = "TU TOKEN WEBHOOKA"



import requests
from discord import Webhook, AsyncWebhookAdapter, RequestsWebhookAdapter
import aiohttp
x = requests.post("http://crusty.pl")
stan_sharda_1 = x.text[13160:13270]
stan_sharda_2 = x.text[13520:13610]    
webhook = Webhook.partial(id_webhooka, token_webhooka,
adapter=RequestsWebhookAdapter())
webhook.send("-----------------------------------------------------------------------------------------")
webhook.send("SHARD 1:" + stan_sharda_1.replace("<", "   ").replace(">", "   ").replace("br", "   "))
webhook.send("SHARD 2:" + stan_sharda_2.replace("<", "   ").replace(">", "   ").replace("br", "   "))
while True:
    x = requests.post("http://crusty.pl")
    stan_sharda_1 = x.text[13160:13270]
    stan_sharda_2 = x.text[13520:13610]
    print("SHARD 1:", stan_sharda_1.replace("<", "   ").replace(">", "   ").replace("br", "   "))
    print("SHARD 2:", stan_sharda_2.replace("<", "   ").replace(">", "   ").replace("br", "   "))
    print("_____________________________________________________________________________________")
    if stan_sharda_1.find("niestabilny") == -1:
        continue
    else:
        webhook = Webhook.partial(id_webhooka, token_webhooka,
        adapter=RequestsWebhookAdapter())
        webhook.send("SHARD 1:", stan_sharda_1.replace("<", "   ").replace(">", "   ").replace("br", "   "))
    if stan_sharda_1.find("pali") == -1:
        continue
    else:
        webhook = Webhook.partial(id_webhooka, token_webhooka,
        adapter=RequestsWebhookAdapter())
        webhook.send("SHARD 1:", stan_sharda_1.replace("<", "   ").replace(">", "   ").replace("br", "   "))
    if stan_sharda_2.find("niestabilny") == -1:
        continue
    else:
        webhook = Webhook.partial(id_webhooka, token_webhooka,
        adapter=RequestsWebhookAdapter())
        webhook.send("SHARD 2:", stan_sharda_2.replace("<", "   ").replace(">", "   ").replace("br", "   "))
    if stan_sharda_1.find("pali") == -1:
        continue
    else:
        webhook = Webhook.partial(id_webhooka, token_webhooka,
        adapter=RequestsWebhookAdapter())
        webhook.send("SHARD 2:", stan_sharda_2.replace("<", "   ").replace(">", "   ").replace("br", "   "))
