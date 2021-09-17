def format_print(olist):
    for args in olist:
        obj = args.__dict__
        for key in obj:
            formatted = f"{key}: {obj[key]}"
            print(formatted)
        print("-"*40 + "\n")
