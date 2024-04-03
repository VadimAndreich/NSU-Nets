import csv
import subprocess
from pythonping import ping


domains = ["yandex.ru", "google.com", "github.com", "stackoverflow.com", "twitch.tv", "vk.com", "youtube.com", "wikipedia.org", "steamcommunity.com", "terraria-game.fandom.com"]

with open("Task_1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Domain", "IP", "Loss", "Average Time"])

    for domain in domains:
        output = ping(domain)
        ip = str(output).split('\n')[0].split(' ')[2][0:-1]
        avg_ms = output.rtt_avg_ms
        loss = output.stats_lost_ratio

        writer.writerow([domain, ip, loss, avg_ms])
