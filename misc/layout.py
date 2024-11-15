def si_prefix(value):
    import math
    if value == 0:
        return "0"
    exponent = int(math.floor(math.log10(abs(value)) // 3) * 3)
    prefix = {
        -24: "y", -21: "z", -18: "a", -15: "f", -12: "p", -9: "n",
        -6: "u", -3: "m", 0: "", 3: "k", 6: "M", 9: "G", 12: "T", 15: "P"
    }
    scaled_value = value / (10 ** exponent)
    return f"{scaled_value:.3g}{prefix.get(exponent, '')}"

lam = 28e-9

###
w = 16 * lam
l = 2 * lam
###

n = 6 * lam

a_s = a_d = w * n

p_s = p_d = 2 * (w + n)

print(f"L={si_prefix(l)} W={si_prefix(w)} AS={si_prefix(a_s)} AD={si_prefix(a_d)} PS={si_prefix(p_s)} PD={si_prefix(p_d)}")