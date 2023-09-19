import decouple
from supabase_py import create_client

url = decouple.config("SUPABASE_URL")
key = decouple.config("SUPABASE_KEY_PUB")
supabase = create_client(supabase_url=url, supabase_key=key)

response1 = supabase.table('story').select("*").execute()
print(type(response1), response1)