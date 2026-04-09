import re

def vc_counter(data):
    data = data.strip()
    data = data.replace("\n","").replace(" ","")
    print (data)
    vp = "[aeiouAEIOU]"
    letter_p = "[a-zA-z]"
    vpc = re.compile(vp)
    lpc = re.compile(letter_p)

    v_counter = 0
    c_counter = 0

    for chr in data:
        if re.match(vpc,chr):
            v_counter += 1
        elif re.match(lpc,chr):
            c_counter += 1

    return v_counter,c_counter
if __name__=="__main__":
    text = """
     Hi, my name is Dev.
     I Love Python.
    """
    vc,cc = vc_counter(text)
    print(f"VOWELS :{vc}\nCONSONANTS: {cc}")

