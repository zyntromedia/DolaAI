SYSTEM_PROMPT = open(".dola/context.md").read()

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Here are outdated packages: {packages_list}. Create PR."}
    ]
)
