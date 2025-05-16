print("to zostanie wypisane najpierw,")
print("a to dopiero potem")
while False:
    print("ten tekst się nigdy nie wypisze")
if False:
    print("ten tekst się nigdy nie wypisze")
should_print = True
while should_print:
    print("Bedzie wypisane tylko raz")
    should_print = False
printed_times = 0
while printed_times <= 2:
    print(f"Wypisane dla {printed_times}")
    printed_times +=1
i = 3
while i <= 10:
    print(i)
    i += 3
k = 1
while k <= 100:
    print(k)
    k *= 2
l = 0
while l < 100:
    print(l)
    l +=2
m = 0
while m < 100:
    print(m)
    m += 7
n = 13
while n < 1000:
    print(n)
    n *=3
o = 0
while o * o < 1000:
    print(o * o)
    o +=1
names = ["Ala", "Basia", "Celina"]
for name in names:
    print("Next name is " + name)
for z in range(5):
    print(z)
for x in range(4):
    print(f"Last {4 - x} juices")
    print("Glup, Glup, Glup")
print("End of juice")

for a in range(1, 3):
    print(a)
for b in range(2, 5):
    print(b)
for c in range (5, 5):
    print(c)
for d in range (1, 6, 2):
    print(d)
for e in range (10, 0, -3):
    print(e)
for f in range(5):
    print(f)
for g in range(5, 10):
    print(g)
for h in range(5, 30, 4):
    print(h)
for p in range (10, 5, -1):
    print(p)
for r in range(20, 0, -2):
    print(r)