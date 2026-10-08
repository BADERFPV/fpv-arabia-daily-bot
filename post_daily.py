import datetime, json, os, pathlib, sys, urllib.request

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
ROLE_ID = os.environ.get("DISCORD_ROLE_ID", "").strip()
BOT_NAME = os.environ.get("BOT_NAME", "FPV Arabia")

if not WEBHOOK_URL:
    sys.exit("DISCORD_WEBHOOK_URL مو موجود")

messages = json.loads((pathlib.Path(__file__).parent / "messages.json").read_text(encoding="utf-8"))
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).date()
message = messages[today.toordinal() % len(messages)]

content = f"<@&{ROLE_ID}>\n{message}" if ROLE_ID else message
payload = {"username": BOT_NAME, "content": content,
           "allowed_mentions": {"roles": [ROLE_ID] if ROLE_ID else []}}

req = urllib.request.Request(WEBHOOK_URL, data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json", "User-Agent": "FPVArabiaDailyBot"}, method="POST")
with urllib.request.urlopen(req) as resp:
    print("تم الإرسال:", resp.status)
