# 🧰 Reforger Mod List Formatter

Convert mod lists from [BattleMetrics Reforger Servers](https://www.battlemetrics.com/servers/reforger/) into JSON format for use in your server config.

---

## Online Python Compiler

Run the formatter instantly using this online compiler:  
[https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/)

---

## How to Use

### 1. Go to BattleMetrics  
Navigate to [https://www.battlemetrics.com/servers/reforger/](https://www.battlemetrics.com/servers/reforger/)

### 2. Select the Mods  
- Find your desired server.
- Click and drag to select all the mods (like the image below).
- Copy them to your clipboard.

![image](https://github.com/user-attachments/assets/9561ad47-c367-4353-beaf-f23cc347a05e)

### 3. Paste into the Code  
Paste your copied list into the `input_input_data` variable in the Python script.

### 4. Run the Script  
Execute the code, and it will generate a JSON-formatted list of mods.

---

## Example Input

```python
input_data = """
RHS - Content Pack 01	0.12.4414	1337C0DE5DABBEEF
RHS - Content Pack 02	0.12.4414	BADC0DEDABBEDA5E
RHS - Status Quo	0.12.4414	595F2BF2F44836FB
"""  
```

## Example Output

```json
[
	{
		"modId": "1337C0DE5DABBEEF",
		"name": "RHS - Content Pack 01",
		"version": "0.12.4414"
	},
	{
		"modId": "BADC0DEDABBEDA5E",
		"name": "RHS - Content Pack 02",
		"version": "0.12.4414"
	},
	{
		"modId": "595F2BF2F44836FB",
		"name": "RHS - Status Quo",
		"version": "0.12.4414"
	}
]
```
