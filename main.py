input_data = """
RHS - Content Pack 01	0.12.4414	1337C0DE5DABBEEF
RHS - Content Pack 02	0.12.4414	BADC0DEDABBEDA5E
RHS - Status Quo	0.12.4414	595F2BF2F44836FB
"""  

lines = input_data.strip().splitlines()

formatted_mods = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) == 3:
        name, version, mod_id = parts
        mod_entry = f"""\t{{\n\t\t"modId": "{mod_id}",\n\t\t"name": "{name}",\n\t\t"version": "{version}"\n\t}}"""
        formatted_mods.append(mod_entry)

output = ",\n".join(formatted_mods)

print("[\n" + output + "\n]")
