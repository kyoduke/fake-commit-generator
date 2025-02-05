import os
import random
from datetime import datetime
from zoneinfo import ZoneInfo


async def generate_commits(path, date):
    os.chdir(path)
    os.system(f"echo {date} >> fake.txt")
    os.system("git add .")
    os.system(f"git commit -m 'fake of {date}'")
    os.system("git push origin master")


project_path = "/home/duque/dev/lixo/my-history/"
rio_timezone = ZoneInfo("America/Sao_Paulo")
number_of_commits = random.randint(2,10)

for _ in range(number_of_commits):
    date_now = datetime.now(tz=rio_timezone)
    generate_commits(project_path, date_now)
