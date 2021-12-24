"""====== format string  ======="""
# string (sentence)
sentence="Joko"
format_str=f"hello{sentence}"
print(format_str)

#boolean
bool=True
format_str=f"booelan={bool}"
print(format_str)

#integer (bilangan bulat)
angka=10231
format_str=f"booelan={angka:d}"
print(format_str)

#flaot(bilangan desimal)
angka=20.12
format_str=f"angka={angka}"
print(format_str)

#bilangan ribuan
angka=2000
format_str=f"ribuan ={angka:,}"
print(format_str)

#flaot(bilangan desimal)
angka=20.12
format_str=f"angka={angka:.4f}"
print(format_str)

#menambahkan  + - (ini bisa pada angka bulat (integer) atau desimal (decimal))
plus=+20
minus=-12.2917
print(f"angka plus={plus:+d}")
print(f"angka minus={minus:-.2f}")

#membuat persen %
angka=0.452
format_str=f"persentase={angka:.2%}"
print(format_str)

#format ke penyimpanan biner,octal,hex
angka=19
format_binary=f"binary dari {angka},adalah ={bin(angka)}"
format_octal=f"octal dari {angka},adalah ={oct(angka)}"
format_hexagonal=f"hexagonal dari {angka},adalah ={hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexagonal)
