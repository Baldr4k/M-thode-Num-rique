from math import *
R = 8.314

T0 = 273.15
Tref = T0 + 25

Hf_A = -100e3
Hf_B = -30e3
Hf_D = -120e3
Hf_E = -250e3
S_A = 20
S_B = 120
S_C = 105
S_D = 110
S_E = 125

# Question 1
Hf_C = -60e3 # A COMPLETER
T = 356 # A COMPLETER
Hreact1 = Hf_C + Hf_D - Hf_A - 2*Hf_B
Sreact1 = S_C + S_D - S_A - 2*S_B
Greact1 = Hreact1 - T*Sreact1
print('Greact1 = %.42f J/mol' % Greact1)

# Question 2
Kreact1 = exp(-Greact1/(R*T))
print('Kreact1 = %.2e' % Kreact1)

# Question 3
Hreact2 = Hf_E - Hf_A - Hf_D
Kreact2_Tref = 6 # A COMPLETER
Kreact2 = exp(log(Kreact2_Tref) - Hreact2/R*(1/T-1/Tref))
print('Kreact2 = %.2e' % Kreact2)

# Question 4
def solve(a, b, c):
	delta = b**2 - 4*a*c
	return [(-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)]
V = 0.6 # A COMPLETER
a = 1 - Kreact2/(Kreact2 + 1) - 4*Kreact1
b = 4*Kreact1
c = -Kreact1

x = solve(a, b, c)[0]
y = x * Kreact2/(Kreact2 + 1)
n_B = 1-2*x
n_C = x
n_D = x-y
n_E = y
print('n_C = %.2e' % n_C)

# Question 5
n_tot = n_B + n_C + n_D + n_E
p_tot = n_tot * R * T / V / 1e5
print('p_tot = %.2e' % p_tot)